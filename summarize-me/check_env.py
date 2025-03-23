import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Fetch environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
s3_bucket = os.getenv("S3_BUCKET_NAME")
heygen_api_key = os.getenv("HEYGEN_API_KEY")
heygen_template_id = os.getenv("HEYGEN_TEMPLATE_ID")

# Print the values (Masked for security)
print("AWS_ACCESS_KEY_ID:", aws_access_key[:4] + "****" if aws_access_key else "Not Found")
print("AWS_SECRET_ACCESS_KEY:", aws_secret_key[:4] + "****" if aws_secret_key else "Not Found")
print("AWS_REGION:", aws_region if aws_region else "Not Found")
print("S3_BUCKET_NAME:", s3_bucket if s3_bucket else "Not Found")
print("HEYGEN_API_KEY:", heygen_api_key[:4] + "****" if heygen_api_key else "Not Found")
print("HEYGEN_TEMPLATE_ID:", heygen_template_id if heygen_template_id else "Not Found")
