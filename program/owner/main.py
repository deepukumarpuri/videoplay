import os
import logging
import random
import asyncio
from script import Script as script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from driver.database import db, Database
from config import ADMINS, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp
import re
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("startedd"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('Movie & Series Studio Chat', url='https://t.me/joinchat/TmzDkDEYo65iMmM1')
            ],
            [
                InlineKeyboardButton('Series', url='https://t.me/joinchat/c7IfwgC6AtdiOGM1'),
                InlineKeyboardButton('Movies', url='https://t.me/joinchat/zqPG0JH27t9jMzI1')
            ],
            [
                InlineKeyboardButton('⌦ Close the Menu ⌫', callback_data="close_data"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
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
            InlineKeyboardButton('Add me to your Chat', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('Series', url='https://t.me/joinchat/c7IfwgC6AtdiOGM1'),
            InlineKeyboardButton('Movies', url='https://t.me/joinchat/zqPG0JH27t9jMzI1')
            ],[
            InlineKeyboardButton('search here movie', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('movie & series studio chat', url='https://t.me/joinchat/TmzDkDEYo65iMmM1')
            ],[
            InlineKeyboardButton('help', callback_data='help'),
            InlineKeyboardButton('about', callback_data='about')
            ],[
            InlineKeyboardButton('⌦ Close the Menu ⌫', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True,
            parse_mode='html'
        )
