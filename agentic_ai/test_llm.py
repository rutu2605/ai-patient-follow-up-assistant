import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrockConverse

load_dotenv()

llm = ChatBedrockConverse(
    model="openai.gpt-5.6-luna",
    region_name="us-east-1",
    temperature=0,
)

response = llm.invoke(
    "Say hello to the CareLoop project in one short sentence."
)

print(response.content)