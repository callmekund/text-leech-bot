import os

API_ID    = os.environ.get("API_ID", "21484008")
API_HASH  = os.environ.get("API_HASH", "336734e723ed5c7824720449780bd00c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
