import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables.")

# /start and /hello command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello world! 👋\nType /help to see what I can do.")

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *About this bot*\n"
        "Created by Meet.\n"
        "This is a demo Telegram bot for IT Lab 3.",
        parse_mode="Markdown"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Help*\n"
        "Available commands:\n"
        "/start or /hello - Greet the user\n"
        "/about - About the bot and author\n"
        "/fact - Get an interesting fact\n"
        "/buttons - Try interactive buttons",
        parse_mode="Markdown"
    )

# /fact command
async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    facts = [
        "Did you know? The first computer bug was an actual moth.",
        "Python is named after Monty Python, not the snake.",
        "Telegram bots can handle thousands of users at once!"
    ]
    import random
    await update.message.reply_text(random.choice(facts))

# /buttons command
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("About", callback_data='about')],
        [InlineKeyboardButton("Fact", callback_data='fact')],
        [InlineKeyboardButton("Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Handle button presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'about':
        await query.edit_message_text(
            "🤖 *About this bot*\nCreated by Meet.\nDemo for IT Lab 3.",
            parse_mode="Markdown"
        )
    elif query.data == 'fact':
        facts = [
            "Did you know? The first computer bug was an actual moth.",
            "Python is named after Monty Python, not the snake.",
            "Telegram bots can handle thousands of users at once!"
        ]
        import random
        await query.edit_message_text(random.choice(facts))
    elif query.data == 'help':
        await query.edit_message_text(
            "🆘 *Help*\n"
            "Available commands:\n"
            "/start or /hello - Greet the user\n"
            "/about - About the bot and author\n"
            "/fact - Get an interesting fact\n"
            "/buttons - Try interactive buttons",
            parse_mode="Markdown"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler(["start", "hello"], start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("buttons", buttons))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()