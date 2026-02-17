import os
from pyexpat.errors import messages

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini")


### Built in middlewares ###

# from langchain.agents import create_agent
# from langchain.agents.middleware import SummarizationMiddleware
# from langgraph.checkpoint.memory import InMemorySaver
# from langchain_core.messages import HumanMessage, SystemMessage

### Message based Summarization ###

# agent = create_agent(model=model,
#                      checkpointer=InMemorySaver(),
#                      middleware=[SummarizationMiddleware(
#                          model=model,
#                          trigger=("messages", 10),
#                          keep=("messages", 4)),],
#                      )

## run with thread_id

# config = {"configurable":{"thread_id": "test-1"}}
#
# questions = [
#     "what  is 10 + 10?, answer in one word",
#     "what is the color of sky, answer in one word",
#     "what is 100/4",
#     "what  is 3*3",
#     "what does ai stand for?",
#     "Who is the president of the United States?"
# ]
#
# for question in questions:
#     response = agent.invoke({
#         "messages":[
#             HumanMessage(content=question)
#         ],
#     },
#     config=config)
#     print(f"Message ; {response}")
#     print(f"Message ; {len(response['messages'])})")



### Human in the loop middleware

from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

def read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its id"""
    return f"Email content for id: {email_id}"


def send_email_tool(recipient: str, subject: str, body: str)->str:
    """Mock function to send an email"""
    return f"Email sent to {recipient} for subject: {subject}"

agent = create_agent(
    model=model,
    tools=[read_email_tool, send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[HumanInTheLoopMiddleware(
        interrupt_on={
            "send_email_tool":
                {
                    "allowed_decisions": ["approve", "edit", "reject"]
                },
            "read_email_tool": False
        }
    ),
    ]
)

config = {"configurable": {"thread_id": "test-approve"}}

result = agent.invoke({"messages":
                       [HumanMessage(content="send email to john@test.com with subject 'Hello' and body 'How are you?'")]},
                      config=config)

print(result)

if "__interrupt__" in result:
    print("Paused --- Approving")
    result = agent.invoke(
        Command(
            resume = {
                "decisions": [
                    {"type": "approve"},
                ]
            }
        ),
        config=config,
    )
    print(f" result: {result['messages'][-1].content}")
