
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Guardrail configuration
MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "5000"))
MAX_OUTPUT_CHARS = int(os.getenv("MAX_OUTPUT_CHARS", "6000"))
