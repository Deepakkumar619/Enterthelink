from telegram.ext import Updater, CommandHandler
from urllib.parse import urlparse

# Function to convert Terabox link to Mdisk Play link
def convert_terabox_to_mdisk_play(terabox_link):
    if "terabox" not in terabox_link:
        return "Invalid Terabox link provided"
    
    terabox_id = urlparse(terabox_link).path.split("/")[-1]
    mdisk_play_link = f"https://mdisk-play.net/video/{terabox_id}"
    
    return mdisk_play_link

# Command handler for /convert command
def convert_command(update, context):
    try:
        terabox_link = context.args[0]
        mdisk_play_link = convert_terabox_to_mdisk_play(terabox_link)
        update.message.reply_text(f"Mdisk Play Link: {mdisk_play_link}")
    except IndexError:
        update.message.reply_text("Please provide a Terabox link.")

# Function to start the bot
def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /convert command
    dp.add_handler(CommandHandler("convert", convert_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
