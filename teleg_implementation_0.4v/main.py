from datetime import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types
from weather_api import weather_forecast
from stocks_api import stocks

API_TOKEN = 'API_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start and restart
@dp.message_handler(commands=['start', 'restart'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Lane!\nWant to be friends with me? :3\nIf you want to know what I can do type /help")

# Weather
@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    forecast = weather_forecast()
    await message.reply(forecast)

# Stocks
@dp.message_handler(commands=['amd'])
async def amd(message: types.Message):
    closes, news = stocks()
    await message.reply(closes)
    if news != 'None':
        for piece in range(0, 3):
            current_message = news[f'news_{piece}']
            formatted_message = f'Author: {current_message[0]}\nTitle: {current_message[1]}\nBody: {current_message[2]}'
            await message.reply(formatted_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)