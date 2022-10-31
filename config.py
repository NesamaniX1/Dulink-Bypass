import os
from dotenv import load_dotenv

load_dotenv()
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# Optionnal variables

WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

