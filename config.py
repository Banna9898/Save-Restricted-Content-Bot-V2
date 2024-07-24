# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29141829"))
API_HASH = getenv("API_HASH", "25020d00fbcfd406fc9979d24d761bff")
BOT_TOKEN = getenv("BOT_TOKEN", "6998826537:AAE24A88dHWSxFLFQ5jFYs2Sq8UwDPtasug")
OWNER_ID = int(getenv("OWNER_ID", "5323404314"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002071932943"))
FORCESUB = getenv("FORCESUB", "jayhind_675")
