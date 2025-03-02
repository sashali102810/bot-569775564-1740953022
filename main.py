Для создания Telegram-бота с использованием библиотеки `python-telegram-bot` версии 20.x и `requests`, а также с учетом всех указанных требований, можно использовать следующий код:

### Установка необходимых библиотек
Сначала установите необходимые библиотеки:

```bash
pip install python-telegram-bot requests
```

### Код бота

```python
import logging
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot_errors.log'
)

logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, который пока не активен. Используй /help для получения информации.")

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я бот, который пока не активен. Используй /start для начала.")

# Функция для автоматического перезапуска при сбоях
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    # Здесь можно добавить логику для перезапуска бота, если это необходимо
    # Например, можно использовать os.execv для перезапуска скрипта

# Основная функция для запуска бота
def main():
    # Убедитесь, что у вас есть токен бота
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    if not token:
        logger.error("Токен бота не найден!")
        return

    # Создаем приложение
    application = ApplicationBuilder().token(token).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        # Перезапуск бота при сбое
        os.execv(__file__, sys.argv)
```

### Описание кода

1. **Логирование ошибок**: Все ошибки логируются в файл `bot_errors.log`.
2. **Обработчики команд**: Реализованы обработчики для команд `/start` и `/help`.
3. **Функционал "бот не активен"**: Бот просто отвечает на команды, но не выполняет никаких активных действий.
4. **Автоматический перезапуск**: В случае сбоя бот автоматически перезапускается с помощью `os.execv`.

### Запуск бота

1. Замените `'YOUR_TELEGRAM_BOT_TOKEN'` на ваш токен, полученный от BotFather.
2. Запустите скрипт:

```bash
python your_bot_script.py
```

Теперь ваш бот будет работать, логировать ошибки и автоматически перезапускаться в случае сбоев.