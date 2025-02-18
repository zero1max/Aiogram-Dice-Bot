# Aiogram Dice Bot  

This is a simple Telegram bot built using Aiogram 3.x. The bot sends various types of dice emojis (football, slot machine, bowling, basketball) to a specified chat when a user sends corresponding commands.  

## Features  
- `/start` - Greets the user  
- `/ball` - Sends 10 football dice rolls  
- `/pot` - Sends 10 slot machine spins  
- `/bow` - Sends a single bowling roll  
- `/bask` - Sends a single basketball throw  
- `/chat_id` - Gets the chat ID  

## Requirements  
- Python 3.10+
- `aiogram` 3.x  

## Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/aiogram-dice-bot.git
   cd aiogram-dice-bot


2. Install dependencies:
   ```sh
   pip install -r requirements.txt


3. Create a .env file and add your bot token:
   ```sh
    BOT_TOKEN=your_bot_token_here
    CHAT_ID=-1001234567890  # Replace with your group chat ID

4. Run the bot:
    ```sh
    python bot.py
