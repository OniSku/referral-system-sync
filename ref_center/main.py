import asyncio
import logging
from scanner.sync import fetch_payments

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def scanning_cycle():
    while True:
        try:
            logger.info("Запуск планового сканирования транзакций...")
            payments = fetch_payments("data/database.db")
            logger.info(f"Обработано {len(payments)} новых транзакций.")
            await asyncio.sleep(300)
        except Exception as e:
            logger.error(f"Ошибка цикла: {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(scanning_cycle())
