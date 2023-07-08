import logging

from loader import dp, bot, logger

from data.config import SKIP_UPDATES

from data.messages import ALERT_STARTUP_MESSAGE, ALERT_SHUTDOWN_MESSAGE

from handlers import (
    set_default_commands,
    register_users_commands,
    register_users_main_menu,
    register_users_pickers,
    register_users_cancels,
    register_users_games,
    register_users_payment,
    register_admins_commands,
)

from database import startup_setup, shutdown_setup

from functions import send_alerts, check_games_info, check_tests_info

from aiogram import Dispatcher
from aiogram.utils import executor


def register_all_handlers(dispatcher: Dispatcher):
    register_users_games(dispatcher)
    register_users_pickers(dispatcher)
    register_users_payment(dispatcher)
    register_users_cancels(dispatcher)
    register_users_main_menu(dispatcher)
    register_users_commands(dispatcher)
    register_admins_commands(dispatcher)


async def on_startup(dispatcher: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Setup PostgreSQL connection')
    await startup_setup()

    logger.info('Checking all games')
    await check_games_info()

    logger.info('Checking all tests')
    await check_tests_info()

    logger.info('Set all default commands')
    await set_default_commands(bot)

    logger.info('Register all handlers')
    register_all_handlers(dispatcher)

    logger.info('Bot starting users alert')
    await send_alerts(text_alert=ALERT_STARTUP_MESSAGE)


async def on_shutdown(dispatcher: Dispatcher):
    logger.info('Bot stopped users alert')
    await send_alerts(text_alert=ALERT_SHUTDOWN_MESSAGE)

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
