import os
import logging
import random
import asyncio
from datetime import datetime
from script import Script as script
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from driver.database import db, Database
from config import *
from utils import get_size, is_subscribed, temp
import re
logger = logging.getLogger(__name__)
from sys import version_info
from time import time
from pyrogram import Client, filters # Ik this is weird as this shit is already imported in line 6! anyway ... Fuck Off!
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from driver.filters import command, other_filters, other_filters2
from driver.database import db, Database
from driver.dbthings import handle_user_status
from config import *




@Client.on_message(filters.command("help"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
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
        await message.reply(script.HELP_TXT.format(message.from_user.mention if message.from_user else message.chat.title, message.chat.username), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
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
        await message.reply_text(
            text=script.HELP_TXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True,
            parse_mode='html'
        )
