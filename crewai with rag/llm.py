from langchain_community.chat_models import ChatLiteLLM
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

user_input = os.getenv('USER_INPUT')
diagram_language = os.getenv('DIAGRAM_LANGUAGE')

OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME')

model = ChatLiteLLM(model=OPENAI_MODEL_NAME)

# content = "Translate this sentence from English to French. I love programming."

# message = HumanMessage(content=content)

# response = model.invoke([message])


# print(response)