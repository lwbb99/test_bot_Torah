import random
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure the logger to display debug information
logging.basicConfig(level=logging.DEBUG)

# Create an instance of the bot and the dispatcher
bot = Bot(token='6056914444:AAEsiJb5yj4rf2PD9hRMteLW0dBi-yX9ucQ')
dp = Dispatcher(bot)

# Load Torah passages from a text file
def load_torah_passages():
    with open('torah_passages.txt', 'r') as file:
        passages = file.readlines()
        passages = [passage.strip() for passage in passages]
    return passages

# Handler to handle the /start command
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    reply_message = "🌟 Welcome to Torah Bot! 📜\n\nI am here to share religious passages from the Torah with you. Just type '/torah' and I will provide you with a random passage. May the wisdom of the Torah guide you! 🙏\n\nTry /info or /commands too. \n\nJoin our currency group, @TORAH_ERC 💰🚀"
    await message.reply(reply_message)

# Handler to handle the /torah command
@dp.message_handler(commands=['torah'])
async def handle_torah(message: types.Message):
    # Load Torah passages
    torah_passages = load_torah_passages()
    
    # Choose a random passage
    passage = random.choice(torah_passages)
    
    reply_message = f"{passage}\n\nJoin our currency group, @TORAH_ERC 💰🚀"
    await message.reply(reply_message)

# Handler to handle the /info command
@dp.message_handler(commands=['info', 'explain'])
async def handle_info(message: types.Message):
    reply_message = '''ℹ️ Torah Bot - Information ℹ️

The Torah is the sacred text of the Jewish people. It consists of the first five books of the Hebrew Bible: Genesis, Exodus, Leviticus, Numbers, and Deuteronomy.

📜 The Torah contains the following key elements:
- Origins: It is believed to have been revealed by God to Moses on Mount Sinai.
- Commandments: The Torah includes the foundational laws and commandments given by God to guide the Jewish people in matters of ethics, worship, and daily life.
- Authorship: Traditionally, it is believed that Moses wrote the Torah under divine inspiration.
- Religion: The Torah is central to Judaism, the religion practiced by Jewish people worldwide.
- Year of Emergence: The Torah has ancient origins, dating back to approximately the 13th century BCE.

In the present day, the Torah remains a cornerstone of Jewish faith, providing moral and spiritual guidance. It continues to be studied, read, and celebrated in Jewish communities around the world.

For a random Torah passage, type '/torah'. Explore the wisdom and teachings of the Torah through this bot. 🙏

Join our currency group, @TORAH_ERC 💰🚀'''
    await message.reply(reply_message)

# Handler to handle the /commands command
@dp.message_handler(commands=['commands'])
async def handle_commands(message: types.Message):
    reply_message = '''📜 Torah Bot - Commands 📜

Here are the available commands:
📜 /start - Start the bot and receive a welcome message.
📜 /torah - Receive a random Torah passage.
📜 /info or /explain - Learn about the Torah, its origins, commandments, religion, and its relevance in the present day.
📜 /commands - View the available commands and their descriptions.

Join our currency group, @TORAH_ERC 💰🚀'''
    await message.reply(reply_message)

# Function to start the bot
def start_bot():
    executor.start_polling(dp, skip_updates=True)

# Call the function to start the bot
if __name__ == '__main__':
    start_bot()