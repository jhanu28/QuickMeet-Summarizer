QuickMeet: AI for Faster Meeting Insights
QuickMeet is an AI-powered tool that transcribes meetings, summarizes key points, extracts action items, and creates video summaries.

🚀 Features
✅ Transcribe meetings with Amazon Transcribe
✅ Summarize notes using Claude 3 Haiku (Amazon Bedrock)
✅ Extract key points & action items
✅ Generate video summaries with HeyGen
✅ Store & search summaries using Weaviate

🛠 Setup
Clone the repository

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt  
Configure AWS & HeyGen credentials in .env

Start the Weaviate vector store:

bash
Copy
Edit
docker compose -f vector_store/weaviate-docker-compose.yaml up -d  
🎯 Usage
Run the script:

bash
Copy
Edit
python app.py  
It will:
✅ Transcribe meetings
✅ Summarize content
✅ Extract key points & action items
✅ Create video summaries
✅ Store & search summaries

📂 Output Files
Transcription: [filename]_transcription.txt

Key Points: [filename]_key_points.txt

Action Items: [filename]_action_items.txt

Video Summary: [filename]_video_summary.mp4

📌 Notes
AWS permissions required for Transcribe, S3, and Bedrock

HeyGen API key needed for video generation
