import os
from dotenv import load_dotenv
from twilio.rest import Client
from openai import OpenAI
from deepgram import Deepgram
import whisper

load_dotenv()

twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
deepgram_client = Deepgram(os.getenv('DEEPGRAM_API_KEY'))
whisper_model = whisper.load_model("base")
