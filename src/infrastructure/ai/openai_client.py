import openai
from infrastructure.config.settings import settings

class OpenAIClient:
    def __init__(self):
        openai.api_key = settings.openai_api_key

    def chat(self, system_prompt: str, user_prompt: str, model="gpt-5"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message["content"]
