# quickmeet-backend/email_sender.py

import boto3
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
SOURCE_EMAIL = os.getenv("SOURCE_EMAIL")  # Your verified sender email

# Create an SES client
ses_client = boto3.client("ses", region_name=AWS_REGION)

def send_meeting_email(to_addresses, subject, summary_text, action_items_text):
    """
    Sends an email using AWS SES with both plain text and HTML content.
    The HTML content includes the meeting summary and action items, with checkboxes next to each action item.
    
    Note: The checkboxes are disabled (non-interactive) because most email clients do not support interactive form elements.
    """
    # Plain text version of the email
    plain_body = f"Meeting Summary:\n{summary_text}\n\nAction Items:\n{action_items_text}"
    
    # Convert action_items_text (assumed newline-separated) into HTML list with checkboxes
    action_items_html = ""
    for item in action_items_text.splitlines():
        if item.strip():
            action_items_html += f'<label><input type="checkbox" disabled> {item}</label><br>'
    
    # If no action items found, show a default message
    if not action_items_html:
        action_items_html = "<p>No action items.</p>"
    
    # HTML version of the email
    html_body = f"""
    <html>
      <body>
        <h2>Meeting Summary</h2>
        <p>{summary_text}</p>
        <h2>Action Items</h2>
        {action_items_html}
      </body>
    </html>
    """
    
    response = ses_client.send_email(
        Source=SOURCE_EMAIL,
        Destination={'ToAddresses': to_addresses},
        Message={
            'Subject': {'Data': subject, 'Charset': 'UTF-8'},
            'Body': {
                'Text': {'Data': plain_body, 'Charset': 'UTF-8'},
                'Html': {'Data': html_body, 'Charset': 'UTF-8'}
            }
        }
    )
    return response
