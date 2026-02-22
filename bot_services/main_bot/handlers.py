from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    args = message.text.split()
    referrer_id = args[1] if len(args) > 1 and args[1].isdigit() else None
    await message.answer("Добро пожаловать! Ваша регистрация подтверждена.")
