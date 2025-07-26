from gradio_client import Client
import requests

from requests.exceptions import ReadTimeout
client = Client("UmarKhattab09/WebScraping_With_LLM_FineTuning")

news = """Before he entered politics, Kennedy made a career out of stoking doubt about vaccines, promoting theories contradicted by mountains of scientific evidence on common vaccines which have been studied for decades and safely administered to hundreds of millions of people.
Now, six months in as head of Health and Human Services, he has instituted a number of policy changes on access to vaccines for both children and adults.
NPR's Mary Louise Kelly and health correspondents Rob Stein and Pien Huang talk through how these changes could impact public health and the public's wallets.
For sponsor-free episodes of Consider This, sign up for Consider This+ via Apple Podcasts or at plus.npr.org.
Email us at considerthis@npr.org.
This episode was produced by Connor Donevan. It was edited by Scott Hensley and Jeanette Woods. Our executive producer is Sami Yenigun.
    """
try:
    print("Calling predict()...")
    result = client.predict(
        news,
        api_name="/trainingllm"
    )
    print("Result:", result)
except Exception as e:
    print("Failed:", e)