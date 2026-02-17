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

# from typing_extensions import TypedDict, Annotated
#
# class Movie(TypedDict):
#     title: Annotated[str, ..., "The title of the movie"]
#     year: Annotated[int, ..., "The year of the movie"]
#     director: Annotated[str, ..., "The director of the movie"]
#     rating: Annotated[float, ..., "The rating of the movie"]
#
# model_with_typed_dict = model.with_structured_output(Movie)
# response = model_with_typed_dict.invoke("Provide details about the movie Avengers")
# print(response)

# from typing_extensions import TypedDict, Annotated
# from pydantic import Field
#
# class Actor(TypedDict):
#     name: str
#     role: str
#
# class MovieDetails(TypedDict):
#     title: str
#     year: int
#     cast: list[Actor]
#     genres: list[str]
#     budget: float | None = Field(None, description="budget in millions USD")
#
# model_with_typed_dict = model.with_structured_output(MovieDetails)
# response = model_with_typed_dict.invoke("Provide details about the movie Avengers")
# print(response)


### Data classes

from pydantic import BaseModel, Field
from langchain.agents import create_agent
from dataclasses import dataclass

@dataclass
class ContactInfo:
    """Contact Information of a person"""
    name: str = Field(description="Name of the person")
    email: str = Field(description="Email address of the person")
    phone: str = Field(description="Phone number of the person")

agent = create_agent(
    model=model,
    response_format=ContactInfo,
)

response = agent.invoke({"messages":[{
    "role": "user",
    "content": "Excract contact info from : John Doe, (555) 123-4567, johndoe@email.com"}]})

print(response["structured_response"])