import os
import resend
from typing import Dict
from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

app = FastAPI()


@app.post("/")
def send_mail() -> Dict:
    params: resend.Emails.SendParams = {
        "from": "onboarding@resend.dev",
        "to": ["delivered@resend.dev"],  # here you can add your own email...
        "subject": "Hello World",
        "html": "<strong>it works!</strong>",
    }
    email: resend.Email = resend.Emails.send(params)
    return email
