from fastapi import APIRouter, Request, Response
from InterviewAgent.app.utility.twilio_handler import generate_twiml_response, handle_stream

router = APIRouter()

@router.post("/voice")
async def voice(request: Request):
    twiml = generate_twiml_response()
    return Response(content=str(twiml), media_type="application/xml")

@router.post("/stream")
async def stream(request: Request):
    return await handle_stream(request)
