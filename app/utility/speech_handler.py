from app.config import whisper_model, deepgram_client
import aiohttp
import base64
import os

async def handle_twilio_audio(audio):
    text = whisper_model.transcribe(audio)["text"]
    return text

async def text_to_speech(text):
    url = "https://api.deepgram.com/v1/speak"
    headers = {
        "Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice": "alpha",
        "model": "enhanced",
        "encoding": "linear16",
        "sample_rate": 8000
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                audio_content = await response.read()
                return base64.b64encode(audio_content).decode('utf-8')
            else:
                raise Exception(f"Deepgram API error: {response.status}")

async def speech_to_text(audio):
    text = whisper_model.transcribe(audio)["text"]
    return text
