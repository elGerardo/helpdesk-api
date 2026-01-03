import os
from dotenv import load_dotenv
from pwdlib import PasswordHash
load_dotenv()

DEBUG = os.getenv("DEBUG", "True")
HASH = PasswordHash.recommended()
