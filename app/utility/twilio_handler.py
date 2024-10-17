from twilio.twiml.voice_response import VoiceResponse, Start
from fastapi import Request, Response
import base64

def generate_twiml_response():
    response = VoiceResponse()
    start = Start()
    start.stream(url='wss://your-domain.com/ws')
    response.append(start)
    response.say('Welcome to the interview. Please wait while we connect you.')
    return response

async def handle_stream(request: Request):
    data = await request.json()
    if data['event'] == 'media':
        audio_chunk = base64.b64decode(data['media']['payload'])
        # Process the audio chunk here
        return Response(content=audio_chunk, media_type="application/octet-stream")
    return Response(status_code=200)
