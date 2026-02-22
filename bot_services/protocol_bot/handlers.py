from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_protocol_service(message: types.Message):
    await message.answer("Сервис подключен. Протоколы синхронизированы.")
