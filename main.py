import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# Masukan API OPENAI & BOT TELEGRAM
openai.api_key = "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"
bot = AsyncTeleBot('5958847106:AAEttrZix9qRne9fj63q_A5LEmzi-ZIlCzI')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hallo, Saya Google tapi versi duanya, Silakan tanya apa aja....\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())
