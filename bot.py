import logging

from loader import dp, bot, logger

from data.config import SKIP_UPDATES

from data.messages import ALERT_STARTUP_MESSAGE, ALERT_SHUTDOWN_MESSAGE

from handlers import (
    register_users_cancels_menu,
    register_users_commands,
    set_default_commands,
    register_main_menu
)

from database import startup_setup, shutdown_setup, get_users_alert

from aiogram import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import (
    BotBlocked,
    ChatNotFound,
    UserDeactivated,
    MigrateToChat,
    Unauthorized,
    BadRequest,
    RetryAfter
)


def register_all_handlers(dispatcher: Dispatcher):
    register_main_menu(dispatcher)
    register_users_cancels_menu(dispatcher)
    register_users_commands(dispatcher)


async def on_startup(dispatcher: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Setup PostgreSQL connection')
    await startup_setup()

    logger.info('Set all default commands')
    await set_default_commands(bot)

    logger.info('Register all handlers')
    register_all_handlers(dispatcher)

    logger.info('Bot starting users alert')
    users_alert = await get_users_alert()
    for user_alert in users_alert:
        user_alert = user_alert[0]
        try:
            await bot.send_message(chat_id=user_alert, text=ALERT_STARTUP_MESSAGE, disable_notification=True)
        except (BotBlocked, ChatNotFound, UserDeactivated, MigrateToChat, Unauthorized, BadRequest, RetryAfter):
            pass


async def on_shutdown(dispatcher: Dispatcher):
    logger.info('Bot stopped users alert')
    users_alert = await get_users_alert()
    for user_alert in users_alert:
        user_alert = user_alert[0]
        try:
            await bot.send_message(chat_id=user_alert, text=ALERT_SHUTDOWN_MESSAGE, disable_notification=True)
        except (BotBlocked, ChatNotFound, UserDeactivated, MigrateToChat, Unauthorized, BadRequest, RetryAfter):
            pass

    logger.info('Closing PostgreSQL connection')
    await shutdown_setup()

    logger.info('Closing storage')
    await dp.storage.close()


if __name__ == '__main__':
    try:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=SKIP_UPDATES
        )
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
        raise
