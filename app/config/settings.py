from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables desde .env

DATABASE_URL = os.getenv("DATABASE_URL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")