import os
import requests


api_key = os.getenv("HEYGEN_API_KEY")
template_id = os.getenv("HEYGEN_TEMPLATE_ID")

url = "https://api.heygen.com/v1/video/generate"  # Adjust if needed
headers = {"Authorization": f"Bearer {api_key}"}
data = {
    "template_id": template_id,
    "script": "Hello, this is a test for QuickMeet!"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())  # Check if the response is valid
