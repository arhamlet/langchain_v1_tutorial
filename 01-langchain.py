import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain.agents import create_agent


def get_weather(city:str)->str:
    """Get the  weather of the city"""
    return f'The weather of the {city} is sunny.'

agent = create_agent(
    model =  "gpt-4o-mini",
    tools=[get_weather],
    system_prompt="You are a helpful assistant.",
)

response = agent.invoke({
"messages" : [
{"role": "user",
"content": "What  is the weather in New York?",
}
]
})

print(response["messages"][-1].content)

