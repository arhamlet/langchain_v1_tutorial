import os
from pyexpat.errors import messages

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini")

from langchain.messages import SystemMessage, AIMessage, HumanMessage

messages  = [
    SystemMessage("You are a poetry expert"),
    HumanMessage("Write a 2 line poem on AI")
]
response = model.invoke(messages)
print(response.content)