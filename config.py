# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "10000844"))
API_HASH = getenv("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = getenv("BOT_TOKEN", "7332530560:AAF_nxrRbiyMu7ImN7Zr-UCEun7fdkX9Gz4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6750546542").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1004592650029")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002061250957"))
