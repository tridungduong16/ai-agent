"""Main module."""
import json
# from llama_index.agent.openai import OpenAIAgent
# from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import logging
import sys
from dotenv import load_dotenv
import os

api_version = os.getenv("api_version")
api_base = os.getenv("api_base_gpt4")
api_key = os.getenv("api_key_gpt4")
api_model = os.getenv("api_model_gpt4")
model = os.getenv("api_engine_gpt4")

llm = AzureOpenAI(
    deployment_name=api_model,
    api_key=api_key,
    azure_endpoint=api_base,
    api_version=api_version,
    engine=model,
)
embed_model = AzureOpenAIEmbedding(
            model="text-embedding-3-large",
            deployment_name="text-embeddings",
            api_key=api_key,
            azure_endpoint=api_base,
            api_version=api_version,
        )

def multiply(a: int, b: int) -> int:
    return a * b
multiply_tool = FunctionTool.from_defaults(fn=multiply)
def add(a: int, b: int) -> int:
    return a + b
add_tool = FunctionTool.from_defaults(fn=add)
agent = OpenAIAgent.from_tools(
    [multiply_tool, add_tool], llm=llm, verbose=True
)
response = agent.chat("What is (121 * 3) + 42?")
print(str(response))



# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
# def get_current_weather(location, unit="fahrenheit"):
#     """Get the current weather in a given location"""
#     if "tokyo" in location.lower():
#         return json.dumps(
#             {"location": location, "temperature": "10", "unit": "celsius"}
#         )
#     elif "san francisco" in location.lower():
#         return json.dumps(
#             {"location": location, "temperature": "72", "unit": "fahrenheit"}
#         )
#     else:
#         return json.dumps(
#             {"location": location, "temperature": "22", "unit": "celsius"}
#         )


# weather_tool = FunctionTool.from_defaults(fn=get_current_weather)