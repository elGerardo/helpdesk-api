import os
from pathlib import Path
from pwdlib import PasswordHash
from dotenv import load_dotenv

# Load .env file from the project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)

DEBUG = os.getenv("DEBUG", "True")
HASH = PasswordHash.recommended()
JWT_HASH = os.getenv("JWT_HASH", "HS256")
JWT_SECRET = os.getenv("JWT_SECRET", "secret")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_LIMIT_SECONDS = int(os.getenv("REFRESH_TOKEN_LIMIT_SECONDS", "60"))