import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini")

from langchain.tools import tool


@tool
def get_weather(location:str)->str:
    """Get the weather at a location."""
    return f' the weather at {location} is sunny'

model_with_tools =  model.bind_tools([get_weather])

### or

# agent = create_agent(
#     model = "gpt-4o-mini",
#     tools = [get_weather],
#     system_prompt="You are a helpful assistant"
# )

messages = [{"role":"user",
            "content": "What is the weather in Boston?"}]
ai_message  = model_with_tools.invoke(messages)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    tool_result  = get_weather.invoke(tool_call)
    messages.append(tool_result)

final_message = model_with_tools.invoke(messages)
print(messages)
print(final_message.text)