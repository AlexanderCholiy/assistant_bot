from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_reply_kb() -> types.ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(types.KeyboardButton(text='Регистрация'),)
    kb_builder.row(
        types.KeyboardButton(
            text='Запросить геолокацию', request_location=True),
        types.KeyboardButton(
            text='Запросить контакт', request_contact=True)
    )
    return kb_builder.as_markup(
        resize_keyboard=True, input_field_placeholder='Регистрация'
    )


def get_inline_yes_no_kb() -> types.ReplyKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        types.InlineKeyboardButton(text='Да'),
        types.InlineKeyboardButton(text='Нет'),
    )
    return kb_builder.as_markup()
