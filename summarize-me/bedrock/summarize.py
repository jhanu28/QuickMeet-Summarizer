import json
import re
from transformers import pipeline

# Load Transcription JSON
with open("QuickMeetTest.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract transcript text
transcribed_text = data["results"]["transcripts"][0]["transcript"]
word_count = len(transcribed_text.split())

# Choose Model Based on Transcript Length
if word_count > 1024:
    model_name = "google/long-t5-tglobal-base"  # For long transcripts
    min_length = max(100, word_count // 4)
    max_length = min(500, word_count // 2)
else:
    model_name = "philschmid/bart-large-cnn-samsum"  # Optimized for meetings
    min_length = max(50, word_count // 3)
    max_length = min(300, int(word_count / 1.5))  # Note: convert to int if needed

print(f"Using Model: {model_name}")
print(f"Min Length: {min_length}, Max Length: {max_length}")

# Load Summarization Model using Hugging Face Transformers (local, not Amazon Bedrock)
summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)

# Generate Summary (consider adding error handling here)
try:
    summary = summarizer(
        transcribed_text,
        min_length=min_length,
        max_length=max_length,
        do_sample=False
    )[0]["summary_text"]
except Exception as e:
    print("An error occurred during summarization:", e)
    summary = "Error: Summarization failed."

# Extract Action Items using regex patterns
action_items = []
task_patterns = [
    r"(\b[A-Z][a-z]+)\s+will\s+(.*?)(?:\.\s|$)",  # Matches "Name will do something"
    r"(\b[A-Z][a-z]+)\s+is\s+responsible\s+for\s+(.*?)(?:\.\s|$)",  # Matches "Name is responsible for..."
    r"Deadline:\s*(\w+\s+\d{1,2})",  # Matches "Deadline: Month Day"
]

names = set()

# Process action items from summary
for pattern in task_patterns:
    matches = re.findall(pattern, summary)
    for match in matches:
        if isinstance(match, tuple):
            name, task = match
            names.add(name)
            action_items.append(f"- {name}: {task.strip()}")
        else:
            action_items.append(f"- {match.strip()}")

# ✅ Fix "He" or "She" by assigning last mentioned name
name_list = list(names)  # Convert set to list to maintain order of appearance
for i, item in enumerate(action_items):
    if item.startswith("- He") or item.startswith("- She"):
        # Look for the most recent name mentioned before the pronoun
        previous_name = next((name for name in reversed(name_list) if name in action_items[i - 1]), "Unknown")
        action_items[i] = item.replace("He: ", f"{previous_name}: ").replace("She: ", f"{previous_name}: ")

# Save summary to summary.txt
with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Save action items to action_items.txt
with open("action_items.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(action_items) if action_items else "No specific action items found.")

print("\n✅ Summary saved to summary.txt")
print("✅ Action Items saved to action_items.txt 🚀")
