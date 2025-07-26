# Model-Context-Protocol

- Understanding of MCP 
- Creating a MCP 

#### Functions added
- simple add function for basic
- added a PINECONE database to perform RAG OPERATIONS
- implemented my huggingface project `WEB SCRAPING LLM FINETUNING` via gradioclient and Fast API. 

## Steps 
- uv init 
- uv add -r requirements.txt
- uvicorn app:app --reload (Need to run FastAPI to fetch the data from the gradioclient. Was not working directly for me )
- You need a dataset that needs to be embedded and uplaoded on a database. I've used PINECONE and a Random PDF. 
- You can use `pinecone.ipynb` to upload the database on pinecone.
- You can use my huggingfacespace.(You can ignore the huggingfacespace folder, I was just trying to understand why gradio client was not working. Turns out I didn't find out. It was working fine on google colab)
- In the end you have to use `uv run mcp install -e main.py` 
- You will see it on the Claude Desktop. You can call it the tools you've created to perform different task

# Future Upgrades
- Probably use a LLM that is not Claude so I can host it on hugggingfacespace.
