import os
from pyexpat.errors import messages

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini")

### PYDANTIC EXAMPLE  ###

# from pydantic import BaseModel, Field
#
# class Movie(BaseModel):
#     title: str = Field(description="The Movie Title")
#     year: int = Field(description="The Year the movie was released")
#     director: str = Field(description="The Director of the Movie")
#     rating: float = Field(description="The Rating of the Movie out of 10")
#
# model_with_structured_outputs = model.with_structured_output(Movie)
# response = model_with_structured_outputs.invoke("Provide details about the movie Inception")
# print(response)


### Message output along parsed structure  ###

# from pydantic import BaseModel, Field
#
# class Movie(BaseModel):
#     title: str = Field(..., description="The Movie Title")
#     year: int = Field(..., description="The Year the movie was released")
#     director: str = Field(..., description="The Director of the Movie")
#     rating: float = Field(..., description="The Rating of the Movie out of 10")
#
# model_with_structured_outputs = model.with_structured_output(Movie, include_raw=True)
# response = model_with_structured_outputs.invoke("Provide details about the movie Inception")
# print(response)


### NESTED STRUCTURE ###

# from pydantic import BaseModel, Field
#
# class Actor(BaseModel):
#     name: str
#     role: str
#
# class MovieDetails(BaseModel):
#     title: str
#     year: int
#     cast: list[Actor]
#     genres: list[str]
#     budget: float | None = Field(None, description="budget in millions USD")
#
# model_with_structured_outputs = model.with_structured_output(MovieDetails)
# response = model_with_structured_outputs.invoke("Provide details about the movie Inception")
# print(response)


### TYPED DICT ###

