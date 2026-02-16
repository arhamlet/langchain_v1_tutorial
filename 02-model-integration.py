import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini")
# print(model)

# from langchain_openai import ChatOpenAI
#
# model = ChatOpenAI(
#     model = "gpt-4o-mini",
# )
# response = model.invoke("Hi, How are you?")
# print(response.content)

### Streaming

# response = model.stream("write a 100 word paragraph on AI")
# for chunk in response:
#     print(chunk.text, end="", flush=True)

### Batch

responses = model.batch(["what is the color of the sky. answer in one wrod",
                        "How do airplanes fly, answer in one line.",
                        "What is quantum computing, reply in one  line."],
                        config={
                            "max_concurrency": 5,
                        })

for response in responses:
    print(response)