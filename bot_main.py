#TODO: создать бота для отправки книг в телеграм
#1)при старте спрашивать имейл для отправки книг
 #   2)принимать файл и по возможносоти конвертировать его в pub формат
  #  3) отправлять файл на указаный имейл
  #4)сделать проверку имейла(reg ex)

import asyncio
import logging
import sys


from handlers import router,dp,bot





async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())