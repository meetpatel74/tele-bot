# Telegram Chat Bot for IT Lab 3

A simple Telegram chatbot built with Python, featuring custom commands, interactive buttons, and secure token management using environment variables.

## Features

- **/start** or **/hello**: Greets the user with "Hello world"
- **/about**: Shows bot and author info
- **/help**: Lists available commands
- **/fact**: Shares a random interesting fact
- **/buttons**: Shows interactive buttons for About, Fact, and Help

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd lab-3
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

Or manually:

```sh
pip install python-telegram-bot python-dotenv
```

### 3. Create a Telegram Bot

- Talk to [@BotFather](https://t.me/botfather) on Telegram
- Use `/newbot` to create a bot and get your API token

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
```

### 5. Run the Bot

```sh
python bot.py
```

## Example Commands

- `/start` or `/hello`
- `/about`
- `/help`
- `/fact`
- `/buttons`

## Screenshots

Add screenshots of your bot in action to the `screenshots/` folder and reference them in your report or README if desired.

## References

- [Official Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial)
- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## License

MIT
