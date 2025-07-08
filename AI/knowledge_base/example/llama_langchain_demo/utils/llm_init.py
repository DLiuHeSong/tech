from langchain.chat_models import ChatOpenAI
import os

def init_llm():
    return ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )