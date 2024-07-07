import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from loguru import logger
load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
logger.add(
        "logs/log.log",
        level="DEBUG",
        rotation="50 MB",
        colorize=True
)

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)
