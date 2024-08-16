from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ɢᴏᴅ : <a href='HTTPS://T.ME/VOATCB'>࿗ VØAT ࿘</a>\n× ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : @Anime_Yugen\n× ᴀɴɪᴍᴇ ɢʀᴏᴜᴘ : @Anime_Yugen_Group\n× ᴍᴀɴɢᴀ ᴄʜᴀɴɴᴇʟ : @Manga_Yugen\n× ᴍᴀɴɢᴀ ɢʀᴏᴜᴘ : @Manga_Yugen_Group\n× ʏᴜɢᴇɴ ɴᴇᴛᴡᴏᴋ : @YugenNetwork\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
