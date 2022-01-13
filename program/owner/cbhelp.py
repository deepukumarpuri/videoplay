
from script import Script as script
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Chat, Message
from config import *
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid




@Client.on_callback_query(filters.regex("cbhelp"))
async def started(_, query: CallbackQuery):
        buttons = [[
            InlineKeyboardButton("🤔 How To Use Me 🤔", callback_data="cbhowtouse")
            ],[
            InlineKeyboardButton("👷🏻 Admin Command", callback_data="cbadmins"),
            InlineKeyboardButton("📚 Basic Command", callback_data="cbbasics")
            ],[
            InlineKeyboardButton("🧙🏻 Sudo Command", callback_data="cbsudos"),
            InlineKeyboardButton("👨‍💻 Owner Command", callback_data="cbowners")
            ],[
            InlineKeyboardButton("📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
            InlineKeyboardButton("👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}")
            ],[
            InlineKeyboardButton('⌦ Close the Menu ⌫', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            disable_web_page_preview=False,
            reply_markup=reply_markup,
            parse_mode='html'
        )
