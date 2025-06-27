from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Bold

from .keyboards import get_reply_kb


router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    content = Text(
        'Здравствуйте, ',
        Bold(message.from_user.full_name)
    )
    await message.answer(**content.as_kwargs())


@router.message(F.text)
async def echo_keyboard(message: types.Message):
    await message.answer('Команды:', reply_markup=get_reply_kb())
