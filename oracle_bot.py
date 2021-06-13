import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboard import oracle_keyboard

from database import do_oracle

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

DB_FILE = 'oracle.db'


async def set_default_commands(dp):
    await dp.bot.set_my_commands([types.BotCommand("start", 'Запустить бота'),
                                  types.BotCommand("help", 'Памагити')])


async def on_startup(dp):
    await set_default_commands(dp)


@dp.message_handler(Command('start'))
async def hello_message(message: Message):
    await message.answer(
        text=f'Привет!\n\n Это мой бот с различными предсказаниями. \n\n Мой ник на GitHub: Nefed-dev')
    await message.answer(text=f'Нажми на одну из кнопок и ты получишь свое предсказание ↓',
                         reply_markup=oracle_keyboard())


@dp.callback_query_handler()
async def oracle(query: CallbackQuery):
    await query.message.edit_text(f'Мое предсказание:\n'
                                  f'\n'
                                  f'{do_oracle(query=query.data)}',
                                  reply_markup=oracle_keyboard())


if __name__ == '__main__':
    try:
        executor.start_polling(dispatcher=dp, on_startup=on_startup)
    except Exception as exc:
        print(exc)
