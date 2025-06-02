# Text Generation Service using LangChain and AWS Bedrock with Claude 3
# This script provides a simple web interface for generating text using the Claude 3 model via AWS Bedrock.
# It includes API key validation, content filtering, and usage logging.

import streamlit as st
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_community.chat_models import BedrockChat

# Load environment variable for API key
load_dotenv()
VALID_API_KEY = os.getenv("VALID_API_KEY")

# Set up AWS credentials
os.environ["AWS_ACCESS_KEY_ID"] = "your-access-key-id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret-access-key"
os.environ["AWS_REGION"] = "us-east-1"

# Bedrock client and Claude 3 model setup
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
llm = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    client=bedrock_client,
    model_kwargs={"temperature": 0.7, "max_tokens": 1024}
)

# Filtering function
BANNED_KEYWORDS = ["violence", "hate", "illegal"]
def content_filter(text):
    return all(word not in text.lower() for word in BANNED_KEYWORDS)

# Log to local file
def log_usage(user_id, prompt):
    with open("usage_log.txt", "a") as log:
        log.write(f"{datetime.utcnow().isoformat()} - {user_id}: {prompt}\n")

# Streamlit UI
st.set_page_config(page_title="Text Generation Service", layout="centered")
st.title("Claude Text Generator (via Bedrock)")

api_key_input = st.sidebar.text_input("Enter API Key", type="password")
user_id = st.sidebar.text_input("User ID", value="anonymous")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if api_key_input != VALID_API_KEY:
        st.error("Invalid API Key")
    elif not content_filter(prompt):
        st.warning("Your prompt contains restricted content.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = llm.invoke(prompt)
                log_usage(user_id, prompt)
                st.success("Response:")
                st.markdown(response.content.strip())
            except Exception as e:
                st.error(f"Error generating response: {e}")


if st.sidebar.checkbox("Show usage log"):
    try:
        with open("usage_log.txt", "r") as log:
            st.sidebar.text_area("Usage Log", log.read(), height=200)
    except FileNotFoundError:
        st.sidebar.info("No logs found yet.")
