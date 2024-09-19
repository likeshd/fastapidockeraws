from fastapi import FastAPI,HTTPException
import uvicorn
import openai
from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")
# Set the OpenAI API key
openai.api_key = api_key

app = FastAPI()

class TranslationRequest(BaseModel):

    input_str: str

def translate_text(input_str):
    completion = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role":"system",
                "content": "You are an expert translator who translate text from English to Marathi and only return translated text"
            },
            {"role":"user", "content": input_str}
        ],
        max_tokens=100,
        temperature=0.7
    )
    return completion.choices[0].message.content

@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.input_str)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500,detail = str(e) )