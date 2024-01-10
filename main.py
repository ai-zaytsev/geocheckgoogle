import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message 
from aiogram.filters import CommandStart
from check.get_address import AddressValidator
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.db_query import *
from settings import settings

TOKEN = settings.bots.bot_token

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()

class Form(StatesGroup):
    Address = State()

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Внести в черный список', callback_data="add_to_black_list")
    keyboard_builder.button(text='Проверить в черном списке', callback_data="check_address_in_black_list")
    keyboard_builder.button(text='Изменить адрес ', callback_data="change_address")

    keyboard_builder.adjust(2,1)

    return keyboard_builder.as_markup()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}, пришли адрес для проверки.")

@dp.message(F.text)
async def return_validated_address(message: Message, state: FSMContext):
    address = AddressValidator()
    validated_address = address.validate_address(message.text)
    await state.update_data(validated_address=validated_address)
    if address.get_validation_granularity(validated_address).lower() == "other":
        await message.answer(f"Похоже, ты прислал невалидный адрес <b>{message.text}</b>, я не могу его найти на гугл-картах. Попробуй еще раз найти этот адрес на гугл-картах и скопировать его оттуда.")
    else:
        await message.answer(f"Отлично, {message.from_user.full_name}, ты прислал адрес <b>{message.text}</b>.\n" \
                            f"В гугл-картах нашелся этот адрес нашелся как <b>{validated_address}</b>.\n" \
                            f"Что ты хочешь сделать?", reply_markup=get_inline_keyboard())

@dp.callback_query(lambda c: c.data == "change_address")
async def reply_for_another_address(callback_query: CallbackQuery):
    await callback_query.answer()  # Отправляем пустое callback_query ответ, чтобы закрыть всплывающее уведомление
    await bot.send_message(callback_query.from_user.id, f"Хорошо, {callback_query.from_user.full_name}, пришли другой адрес и выбери потом, что ты хочешь с ним сделать.")

#проверка адреса на наличие в черном списке
@dp.callback_query(lambda c: c.data == "check_address_in_black_list")
async def check_address_button(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await bot.answer_callback_query(callback_query.id)
    if address_exists(data.get('validated_address')):
        await bot.send_message(callback_query.from_user.id, f"Адрес <b>{data.get('validated_address')}</b> есть в черном списке! Будьте осторожны, заключая договор аренды в этом доме.")
    else:
        await bot.send_message(callback_query.from_user.id, f"Адреса <b>{data.get('validated_address')}</b> не найдено в черном списке.")

#добавление адреса в черный список
@dp.callback_query(lambda c: c.data == "add_to_black_list")
async def add_address_button(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await bot.answer_callback_query(callback_query.id)
    if address_exists(data.get('validated_address')):
        await bot.send_message(callback_query.from_user.id, f"Адрес <b>{data.get('validated_address')}</b> есть в черном списке! Будьте осторожны, заключая договор аренды в этом доме.")
    else:
        add_address(data.get('validated_address'))
        await bot.send_message(callback_query.from_user.id, f"Адрес <b>{data.get('validated_address')}</b> успешно добавлен в черный список! Теперь другие люди будут аккуратнее, заключая договоры аренды в этом доме.")

async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
