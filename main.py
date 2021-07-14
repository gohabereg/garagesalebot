from dotenv import load_dotenv
from garagesalebot.bot import Bot
from garagesalebot.db import DB

load_dotenv()

db = DB()
bot = Bot()