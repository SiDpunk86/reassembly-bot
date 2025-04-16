
import logging
import openai
import telebot

# 🔐 ВСТАВЬ СЮДА СВОИ КЛЮЧИ
TELEGRAM_BOT_TOKEN = "вставь_сюда_твой_токен"
OPENAI_API_KEY = "вставь_сюда_твой_OpenAI_API_ключ"

openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Включаем логирование
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👽 Привет! Я твой Помощник по Пересборке.
Просто задай вопрос — и мы пересоберём твой мир вместе.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты философский помощник, говоришь просто, мудро и по делу."},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "⚠️ Ошибка: " + str(e))

bot.polling()
