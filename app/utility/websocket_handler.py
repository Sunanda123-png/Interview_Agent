from fastapi import APIRouter, WebSocket
from app.speech_handler import handle_twilio_audio, text_to_speech
from app.llm_handler import generate_llm_response, analyze_response

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            message_type = data.get('type')

            if message_type == 'twilio_audio':
                text = await handle_twilio_audio(data['audio'])
                analysis = await analyze_response(text)
                response = await generate_llm_response(analysis)
                speech = await text_to_speech(response)
                await websocket.send_json({
                    'type': 'interviewer_response',
                    'audio': speech
                })
            # Add more message types as needed

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
