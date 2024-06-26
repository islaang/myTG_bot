from aiogram import Bot, Dispatcher
from database.models import models_main
from config import TOKEN
from database.models import models_main
import asyncio
from handlers.commands import router
from parcingmain import *
import logging
import sys



async def main():
    bot = Bot(token=TOKEN) 
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot) #Держит бота в активном состоянии
    # await models_main()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    try:
        asyncio.run(main())
    except Exception as e:
        print("Ошибка",e)
