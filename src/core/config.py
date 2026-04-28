import os
from dotenv import load_dotenv

load_dotenv()

KIMI_API_KEY: str = os.getenv("KIMI_API_KEY", "")
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "kimi-k2-5")
DEFAULT_PROVIDER: str = os.getenv("DEFAULT_PROVIDER", "openclaw")
OPENCLAW_BASE_URL: str = os.getenv("OPENCLAW_BASE_URL", "http://localhost:8000/v1")
