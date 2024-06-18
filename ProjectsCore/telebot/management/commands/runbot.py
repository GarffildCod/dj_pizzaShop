

from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
import requests
from telebot.models import UserBot

class Command(BaseCommand):
    help = 'Запускает телеграм-бота'

    def handle(self, *args, **options):
        # Получение токена бота из настроек Django
        token = settings.TELEGRAM_BOT_TOKEN

        # Создание объекта ApplicationBuilder и передача ему токена бота
        app = ApplicationBuilder().token(token).build()

        # Определение обработчика команды /start
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Получение информации о чате, в котором была отправлена команда /start
            chat = update.effective_chat
            if chat:
                chat_id = chat.id
        # Отправка сообщения пользователю с его chat_id
                await update.message.reply_text(f'Добро пожаловать, {update.effective_user.first_name}!\nВаш chat_id: {chat_id}\nСвяжитесь с владельцем ресурса для получения полного доступа')
            else:
                await update.message.reply_text('Извините, но я не могу определить ваш чат_id.')

        # Регистрация обработчика команды /start
        app.add_handler(CommandHandler("start", start))

        # Определение обработчика команды /hello
        async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text(f'Hello {update.effective_user.first_name}')

        # Регистрация обработчика команды /hello
        app.add_handler(CommandHandler("hello", hello))

        # Запуск бота
        app.run_polling()


def send_telegram_message_to_all(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = chat_ids = UserBot.objects.values_list('chat_id', flat=True)
    print(chat_id)
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
    } 
    response = requests.post(url, data=data)
    return response.json() 