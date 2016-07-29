# =====================================================================================================================================================
# Pokebot will randomly have pokemon appear in chats.
#   Only 151 are here
# ** MUST HAVE pyTelegramBotAPI : [pip install pyTelegramBotAPI] or upgrade [pip install pytelegrambotapi --upgrade]
# ** MUST HAVE tinydb : [pip install tinydb] and numpy
# How to run: python3 pokebot.py 
# =====================================================================================================================================================

# Import libs
import telebot
import configparser
from tinydb_interface import TinyDbInterface
import random

# Parse config file to get the API key
config = configparser.ConfigParser()
config.read("pokebot.cfg")

TOKEN = config['telegram_bot_API']['API_TOKEN']

# Declare bot
bot = telebot.TeleBot(TOKEN)

# Frequency of a pokemon appearing
f = 0.15

# Message handler for when a user will /join the pokemon ...quest? .......
@bot.message_handler(commands=['join'])
def join_action(message):
    tinydb_interface.AddUser()
    bot.reply_to(message, "Catch the pokemon when they appear!")

# Message handler for /start and /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Catch the pokemon when they appear!")

# Message handler for when a user will /catch a pokemon
@bot.message_handler(commands=['catch'])
def send_catch_action(message):
    tinydb_interface.AddPokemon()

    # If empty or not registered
    
    bot.reply_to(message, "Catch the pokemon when they appear!")

# Bot waits for events
print("Pokebot is running...")
bot.polling()
