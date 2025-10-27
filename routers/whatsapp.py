from fastapi import APIRouter, Depends, HTTPException, Form
from langchain.chat_models import init_chat_model
from ..dependencies import get_token_header
from twilio.twiml.messaging_response import MessagingResponse
import os

router = APIRouter(
    prefix="/webhook",
    tags=["whatsapp"],
    #dependencies=[Depends(get_token_header)],
    # default responses to certain codes
    responses={404: {"description": "Not found"}},
)

# Read required environment variables explicitly so failures are obvious
MODEL_NAME = os.environ.get("MODEL_NAME")
MODEL_PROVIDER = os.environ.get("MODEL_PROVIDER")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not MODEL_NAME or not MODEL_PROVIDER or not OPENAI_API_KEY:
    # Fail fast with a clear error message so the container logs show what's missing
    raise RuntimeError(
        "Missing required environment variables: MODEL_NAME, MODEL_PROVIDER, OPENAI_API_KEY"
    )

# Use keyword args to match the expected signature of init_chat_model
model = init_chat_model(model=MODEL_NAME, model_provider=MODEL_PROVIDER, api_key=OPENAI_API_KEY)


from fastapi import APIRouter, Form
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse


@router.post("/whatsapp")
async def whatsapp_twilio(Body: str = Form(...), From: str = Form(...)):
    print(f"📩 Message from {From}: {Body}")

    # Generate your AI response
    response_text = model.invoke(f"Responde a cualquier cosa como un asistente de yazoo veterinaria muy amable, resolviendo dudas de clientes con sus mascotas y reponde que tienes horarios de lunes a viernes de 10am a 4 pm, si te hablan de temas fuera de lo anterior reponse que en que mas los puedes ayudar: {Body}").content

    # Build the Twilio XML (TwiML)
    twilio_response = MessagingResponse()
    twilio_response.message(response_text)

    # Return XML with proper content-type
    return Response(content=str(twilio_response), media_type="application/xml")

