from app.config import openai_client

async def generate_llm_response(text):
    response = await openai_client.completions.create(
        model="text-davinci-002",
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

async def analyze_response(text):
    analysis = await openai_client.completions.create(
        model="text-davinci-002",
        prompt=f"Analyze the following interview response: {text}",
        max_tokens=150
    )
    return analysis.choices[0].text.strip()
