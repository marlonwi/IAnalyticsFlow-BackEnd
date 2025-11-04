from interfaces.api.fastapi_app import app
from dotenv import load_dotenv
import os

load_dotenv()  # 🔹 Carrega as variáveis do .env
api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
