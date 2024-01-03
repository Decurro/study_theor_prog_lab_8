# -*- coding: utf-8 -*-
from loguru import logger
from datetime import datetime
from Bot import Bot


if __name__ == "__main__":
    start_time = datetime.now()
    bot_name = "onlinecontract"
    bot = Bot(bot_name=bot_name)

    try:
        bot.run()

        finish_time = datetime.now()
        logger.info(f"Бот отработал за {finish_time - start_time}")
        exit(0)

    except Exception as err:

        finish_time = datetime.now()
        logger.error(f"Бот упал с ошибкой: {err}")
        logger.info(f"Бот отработал до ошибки за время {finish_time - start_time}")

        exit(1)

