from langchain_community.chat_models import ChatLiteLLM
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-1234"
os.environ["OPENAI_MODEL_NAME"] ='llama3'
os.environ["OPENAI_API_BASE"] ='http://10.35.151.101:8001/v1'

user_input = os.getenv('USER_INPUT')
diagram_language = os.getenv('DIAGRAM_LANGUAGE')

# OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME')

# model = ChatOpenAI(model="llama-3.1-70b-versatile", base_url="https://api.groq.com/openai/v1", api_key="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")

model = ChatOpenAI(model="ibm-llama3-70b", base_url="http://10.35.151.101:8001/v1", api_key="sk-1234")

# content = "Translate this sentence from English to French. I love programming."

# message = HumanMessage(content=content)

# response = model.invoke([message])


# print(response)