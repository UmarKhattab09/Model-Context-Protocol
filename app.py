from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()
client = Client("UmarKhattab09/WebScraping_With_LLM_FineTuning")

class NewsInput(BaseModel):
    text: str

@app.post("/predict_news")
def predict_news(news: NewsInput):
    label, score = client.predict(news.text, api_name="/trainingllm")
    return {
        "category": label,
        "score": score
    }


