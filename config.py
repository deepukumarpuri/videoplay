import os
from os import getenv
from os import environ
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DKBOTZ")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "DKBOTZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")

#MONGA DB URL
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_URI = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Watermarks")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n\n<b>Size:</b> {file_size}\n\n{file_caption}\n\n<b>[© TVSeries & Movie Studio](https://t.me/joinchat/prE6ALN6x2hkY2E1)</b>")


#IMDB SETTINGS
IMDB_TEMPLATE = getenv("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a>\n<b>📺 Type:</b> {kind}\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n<b>🎭 Genres:</b> {genres}\n\n<b>☀️ Languages:</b> {languages}\n<b>🎛 Countries:</b> {countries}\n<b>🎥 Director:</b> {director}\n<b>📝 Writers:</b> {writer}\n\n<b>© Powered by: <a href='https://t.me/+y53tWFUw6Q43NzE9'>{message.chat.title}</a></b>\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 5 minutes to avoid copyright issues.</s>")
IMDB = getenv("IMDB", "True")
LONG_IMDB_DESCRIPTION = getenv("LONG_IMDB_DESCRIPTION", "False")
P_TTI_SHOW_OFF = getenv("P_TTI_SHOW_OFF", "True")
SPELL_CHECK_REPLY = getenv("SPELL_CHECK_REPLY", "True")
SINGLE_BUTTON = getenv("SINGLE_BUTTON", "True")
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)

OWNER_ID = int(os.environ.get("OWNER_ID"))
ADMINS = int(os.environ.get("OWNER_ID"))
# Bot settings

CACHE_TIME = os.environ.get("CACHE_TIME", 300)
USE_CAPTION_FILTER = os.environ.get("USE_CAPTION_FILTER", False)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
PICS = getenv("PICS", "https://telegra.ph/file/be5f551acb116292d15ec.png")

AUTH_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
