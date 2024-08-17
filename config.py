# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29141829"))
API_HASH = getenv("API_HASH", "25020d00fbcfd406fc9979d24d761bff")
BOT_TOKEN = getenv("BOT_TOKEN", "7533852833:AAFbM51a-wGYT79C-HX8Cb1frUpyJBZ4O5E")
OWNER_ID = int(getenv("OWNER_ID", "5323404314"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://forward:forward@cluster0.xowzpr4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002071932943"))
FORCESUB = getenv("FORCESUB", "jayhind_675")
