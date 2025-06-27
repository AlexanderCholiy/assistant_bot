import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from assistant_bot.config import app_config
from users.handlers import router as user_router


async def main():
    """Запускаем бота и пропускаем все накопленные входящие сообщения"""
    bot = Bot(
        app_config.BOT_TOKEN,
        default=DefaultBotProperties(ParseMode.MARKDOWN_V2)
    )
    dp = Dispatcher()
    dp.include_routers(user_router,)

    if app_config.DEBUG:
        logging.basicConfig(level=logging.INFO)

    async with bot:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
