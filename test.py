import os 
import sys
import pathlib
from dotenv import load_dotenv
from pinecone import Pinecone
import os
from dotenv import load_dotenv

# Automatically get the path to your script (main.py) and construct env path
base_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(base_dir, "database", ".env")
load_dotenv(dotenv_path=env_path)
from langchain_community.embeddings import HuggingFaceEmbeddings


# model_name = "thenlper/gte-small"
# embedding_model = HuggingFaceEmbeddings(
# model_name=model_name,
# multi_process=False,
# model_kwargs={"device": "cpu"},
# encode_kwargs={"normalize_embeddings": True},  # Set `True` for cosine similarity
# )



# def pine():
#     PINECONE = os.getenv("PINECONE")
#     pc = Pinecone(api_key=PINECONE)
#     index = pc.Index("vectorized")
#     vectorized_input = embedding_model.embed_query("WHAT IS AI")
#     print(vectorized_input)
#     context = index.query(
#     namespace="GoogleData",
#     vector=vectorized_input,
#     top_k=1,
#     include_metadata=True
# )
#     return context['matches'][0]['metadata']['text']

# print(pine())


# def google(user_input:str)->str:
#     """ When user ask about GOOGLE CLOUD AI FRAME WORK """

#     PINECONE = os.getenv("PINECONE")
#     pc = Pinecone(api_key=PINECONE)
#     index = pc.Index("vectorized")

#     model_name = "thenlper/gte-small"
#     embedding_model = HuggingFaceEmbeddings(
#     model_name=model_name,
#     multi_process=False,
#     model_kwargs={"device": "cpu"},
#     encode_kwargs={"normalize_embeddings": True},  # Set `True` for cosine similarity
# )
    
#     vectorized_input = embedding_model.embed_query(user_input)
#     context = index.query(
#     namespace="GoogleData",
#     vector=vectorized_input,
#     top_k=1,
#     include_metadata=True
# )
#     return context
# print(google("What is AI"))





def google(user_input:str)->str:
    """ When user ask about GOOGLE CLOUD AI FRAME WORK """

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

print(google("wHAT IS AI"))