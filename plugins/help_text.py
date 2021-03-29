import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://t.me/HxBots")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/HxSupport"),
                                                    InlineKeyboardButton(text="SHARE ♐️", url="tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0A__Today%20i%20just%20found%20out%20an%20intresting%20and%20Powerful__%20%2A%2AZee5%20Downloader%20Bot%2A%2A%20__for%20Free%F0%9F%A5%B0.__%20%20%0A%2A%2ABot%20Link%20%3A%20%40Zee5HEXBot%2A%2A%20%F0%9F%94%A5")]]),
    )

@Client.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        
   )

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
