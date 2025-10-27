import asyncio
import logging
from handlers import router,dp,bot
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.WARNING)
    asyncio.run(main())