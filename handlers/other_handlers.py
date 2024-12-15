from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router = Router()

@router.message()
async def not_handler(message: Message):
    await message.answer(
        text=LEXICON['not_handler']
    )