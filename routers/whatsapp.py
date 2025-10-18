from fastapi import APIRouter, Depends, HTTPException, Form
from langchain.chat_models import init_chat_model
from ..dependencies import get_token_header
from twilio.twiml.messaging_response import MessagingResponse
import os

router = APIRouter(
    prefix="/whatsapp",
    tags=["whatsapp"],
    #dependencies=[Depends(get_token_header)],
    # default responses to certain codes
    responses={404: {"description": "Not found"}},
)

model = init_chat_model(os.environ.get("MODEL_NAME"),
                        model_provider=os.environ.get("MODEL_PROVIDER"),
                        api_key=os.environ.get("OPENAI_API_KEY"))


@router.post("/whatsapp")
async def whatsapp_webhook(Body: str = Form(...), From: str = Form(...)):
    print(f"Message from {From}: {Body}")

    response_text = model.invoke(f"Respond conversationally to: {Body}").content

    twilio_response = MessagingResponse()
    twilio_response.message(response_text)
    return str(twilio_response)
