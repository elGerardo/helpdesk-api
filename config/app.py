import os
from dotenv import load_dotenv
from pwdlib import PasswordHash
load_dotenv()

DEBUG = os.getenv("DEBUG", "True")
HASH = PasswordHash.recommended()
JWT_HASH = os.getenv("JWT_HASH", "HS256")
JWT_SECRET = os.getenv("JWT_SECRET", "secret")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))