import json
import re
from transformers import pipeline

def generate_summary(transcript_text):
    """
    Generate a summary from the provided transcript text.
    Returns the summary string.
    """
    word_count = len(transcript_text.split())

    # Use a longer-context model if transcript is longer than 500 words
    if word_count > 500:
        model_name = "google/long-t5-tglobal-base"
        min_length, max_length = max(100, word_count // 4), min(500, word_count // 2)
    else:
        model_name = "philschmid/bart-large-cnn-samsum"
        min_length, max_length = max(50, word_count // 3), min(300, int(word_count // 1.5))
    
    print(f"Using Model: {model_name} for summary generation.")
    try:
        summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)
    except Exception as e:
        raise Exception(f"Model {model_name} loading failed: {e}")
    
    try:
        summary = summarizer(
            transcript_text,
            min_length=min_length,
            max_length=max_length,
            do_sample=False
        )[0]["summary_text"]
    except Exception as e:
        raise Exception(f"Summarization process failed: {e}")
    
    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)
    
    return summary

def extract_action_items(summary_text):
    """
    Extracts action items from the summary text using LLM-based classification and regex.
    Returns a string containing the action items.
    """
    from transformers import pipeline

    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    action_candidates = summary_text.split(". ")
    action_items = []

    labels = ["action item", "discussion", "information", "deadline"]

    for sentence in action_candidates:
        sentence = sentence.strip()
        if not sentence:
            continue

        result = classifier(sentence, labels)
        top_label = result["labels"][0]
        if top_label == "action item" or "will" in sentence or "responsible" in sentence:
            action_items.append(f"- {sentence.strip('.')}.")

    # Fallback regex for deadlines
    deadlines = re.findall(r"Deadline:\s*(\w+\s+\d{1,2})", summary_text)
    for deadline in deadlines:
        action_items.append(f"- Deadline noted: {deadline}")

    # Simple pronoun resolution
    for i in range(1, len(action_items)):
        if action_items[i].startswith("- He") or action_items[i].startswith("- She"):
            prev_name = re.findall(r"- (\b[A-Z][a-z]+):", action_items[i - 1])
            if prev_name:
                action_items[i] = action_items[i].replace("He", prev_name[-1]).replace("She", prev_name[-1])

    result = "\n".join(action_items) if action_items else "No specific action items found."

    with open("action_items.txt", "w", encoding="utf-8") as file:
        file.write(result)

    return result
