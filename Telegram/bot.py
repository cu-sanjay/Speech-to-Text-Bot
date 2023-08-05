import telebot
import config
import logging
from audio_processing import process_voice_message
from telebot.types import Message

# Initialize the Telegram Bot
bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

# Enable logging
logging.basicConfig(filename=config.LOG_FILE, level=config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

# File Make Mode Flag
file_make_mode_enabled = False
file_make_mode_content = ""

# Handler for the /start command
@bot.message_handler(commands=['start'])
def handle_start(message: Message):
    bot.send_message(message.chat.id, "Welcome to the Speech-to-Text Bot!")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def handle_help(message: Message):
    help_message = "Instructions:\n" \
                   "/link <URL> - Download a file from a link.\n" \
                   "/makefile - Enable 'File Make Mode' to create a text file from messages.\n" \
                   "/cancel - Cancel 'File Make Mode'.\n" \
                   "[Send a voice message] - Transcribe voice messages to text."
    bot.send_message(message.chat.id, help_message)

# Handler for the /link command
@bot.message_handler(commands=['link'])
def handle_link(message: Message):
    if len(message.text.split()) == 2:
        url = message.text.split()[1]
        # Download the file from the URL and send it as a document
        # Implement this functionality based on your requirements
    else:
        bot.send_message(message.chat.id, "Please provide a valid URL after the /link command.")

# Handler for the /makefile command
@bot.message_handler(commands=['makefile'])
def handle_makefile(message: Message):
    global file_make_mode_enabled, file_make_mode_content
    file_make_mode_enabled = True
    file_make_mode_content = ""
    bot.send_message(message.chat.id, "File Make Mode is enabled. Send a series of text messages to create a file. "
                                      "The first line will be the file name, and the rest will be the content.")

# Handler for the /cancel command
@bot.message_handler(commands=['cancel'])
def handle_cancel(message: Message):
    global file_make_mode_enabled, file_make_mode_content
    file_make_mode_enabled = False
    file_make_mode_content = ""
    bot.send_message(message.chat.id, "File Make Mode is canceled.")

# Handler for text messages during 'File Make Mode'
@bot.message_handler(func=lambda message: file_make_mode_enabled and message.text)
def handle_file_make_mode_text(message: Message):
    global file_make_mode_content
    if file_make_mode_content == "":
        file_make_mode_content = message.text + "\n"
        bot.send_message(message.chat.id, "The first line is taken as the file name. Continue sending the content.")
    else:
        file_make_mode_content += message.text + "\n"

# Handler for voice messages
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message: Message):
    global file_make_mode_enabled, file_make_mode_content
    if file_make_mode_enabled:
        bot.send_message(message.chat.id, "File Make Mode is still enabled. Please cancel it to process voice messages.")
    else:
        file_path = bot.download_voice(message.voice.file_id)
        text = process_voice_message(file_path)
        bot.send_message(message.chat.id, "Transcription:\n" + text)

# Start the bot
bot.polling(none_stop=True)
