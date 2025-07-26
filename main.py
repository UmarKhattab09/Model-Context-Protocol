from mcp.server.fastmcp import FastMCP
from langchain_community.embeddings import HuggingFaceEmbeddings
from gradio_client import Client

from dotenv import load_dotenv
# envpath = "./database/.env"
import os
import sys
from pinecone import Pinecone
# load_dotenv(envpath)
# Automatically get the path to your script (main.py) and construct env path
base_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(base_dir, "database", ".env")
load_dotenv(dotenv_path=env_path)
# Create an MCP server
mcp = FastMCP("MCPPROJECT")

import requests

from requests.exceptions import ReadTimeout


# Add an addition tool

@mcp.tool()
def google(user_input:str)->str:
    """ When a user ask information about GOOGLE AI
        Input:
            User Message: <User-input>
        Output:
            Text: <Relating to the query>
    
    """

    PINECONE = os.getenv("PINECONE")
    pc = Pinecone(api_key=PINECONE)
    index = pc.Index("vectorized")

    model_name = "thenlper/gte-small"
    embedding_model = HuggingFaceEmbeddings(
    model_name=model_name,
    multi_process=False,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},  # Set `True` for cosine similarity
)
    
    vectorized_input = embedding_model.embed_query(user_input)
    context = index.query(
    namespace="GoogleData",
    vector=vectorized_input,
    top_k=1,
    include_metadata=True
)
    return context['matches'][0]['metadata']['text']

    


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def newsdetection(news:str)->str:
    """
    Runs when the user ask for a category based on the news text
    Input : <USER INPUT> #USER INPUT is a news text that the user provides
    Output : Category  <Categoryoutput>
                Score: <scoreoutput>
    """

    url = "http://127.0.0.1:8000/predict_news"
    data = {
        "text": news
}

    response = requests.post(url, json=data)
    test = response.json()

    return f"{test['category']} {str(test['score'])}"

