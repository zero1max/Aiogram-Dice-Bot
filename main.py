import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

BOT_TOKEN = "YOUR_BOT_TOKEN"

CHAT_ID = 'YOUR_GROUP_ID'

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def start_handler(message: Message):
    await message.reply(f"Assalomu alekum {message.from_user.full_name}")


async def send_bot_ball(message: Message, bot: Bot):
    for _ in range(10):
        await bot.send_dice(CHAT_ID, emoji=DiceEmoji.FOOTBALL)


async def send_bot_pot(message: Message, bot: Bot):
    for _ in range(10):
        await bot.send_dice(CHAT_ID, emoji=DiceEmoji.SLOT_MACHINE)

async def send_bot_bow(message: Message, bot: Bot):
    await bot.send_dice(CHAT_ID, emoji=DiceEmoji.BOWLING)

async def send_bot_bask(message: Message, bot: Bot):
    await bot.send_dice(CHAT_ID, emoji=DiceEmoji.BASKETBALL)

async def get_chat_id(message: Message):
    await message.answer(f"Guruh ID: {message.chat.id}")


# commands register
dp.message.register(start_handler, Command("start"))
dp.message.register(send_bot_ball, Command("ball"))
dp.message.register(send_bot_pot, Command("pot"))
dp.message.register(send_bot_bow, Command("bow"))
dp.message.register(send_bot_bask, Command("bask"))
dp.message.register(get_chat_id, Command("chat_id"))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
