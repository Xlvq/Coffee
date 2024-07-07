import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.settings import logger, bot

from src.start.router import router as start_router


@logger.catch
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        start_router
    )
    # await bot.delete_webhook(drop_pending_updates=True)
    r = await bot.get_me()
    logger.info(f"Бот запущен: https://t.me/{r.username}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
