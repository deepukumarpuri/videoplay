# Copyright (C) 2021 By @DKBOTZ And Some Creadit To VEEZMUSIC

from script import Script as script
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Chat, Message
from config import *
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid


@Client.on_callback_query(filters.regex("cbstartsbyveez"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Allows You To Play Music And Video On Groups Through The New Telegram's Video Chats!**

**๐ก Find Out All The Bot's Commands And How They Work By Clicking On The ยป ๐ Commands Button!**

**๐ To Know How to Use This Bot, Please Click On The ยป โ Basic Guide button!**\n\n You Can Also Watch This Tutorial Video\n In English Voice :- {EN_VIDEO_LINK} \n In Hindi Voice :- {VIDEO_LINK}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("โค๏ธ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "โฆ Close the Menu โซ", callback_data="close_data"
                    )
                ],
            ]
        ),
        disable_web_page_preview=False,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป Admin Commands", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป Sudo Commands", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ Basic Commands", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the basic commands:

ยป /mplay (song name/link) - play music on video chat
ยป /stream (query/link) - stream the yt live/radio live music
ยป /vplay (video name/link) - play video on video chat
ยป /vstream - play live video from yt live/m3u8
ยป /playlist - show you the playlist
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link

ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in group)

ยป /ytthumb (Youtube Link) - Download Youtube Thumbnail Ex :- /ytthumb {EN_VIDEO_LINK}
ยป /vc - Get Your Group VC Link (Only For Public group)
ยป /tts - Reply The Text To Bot Convert in Voice ( Support All Language)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:

ยป /pause - pause the stream
ยป /resume - resume the stream
ยป /skip - switch to next stream
ยป /stop - stop the streaming
ยป /vmute - mute the userbot on voice chat
ยป /vunmute - unmute the userbot on voice chat
ยป /volume `1-200` - adjust the volume of music (userbot must be admin)
ยป /reload - reload bot and refresh the admin data
ยป /userbotjoin - invite the userbot to join group
ยป /userbotleave - order userbot to leave from group

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /sysinfo - show the system information
ยป /update - update your bot to latest version
ยป /restart - restart your bot
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("You're An Anonymous Admin !\n\nยป Revert Back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **Settings Of** {query.message.chat.title}\n\nโธ : Pause Stream\nโถ๏ธ : Resume Stream\n๐ : Mute Userbot\n๐ : Unmute Userbot\nโน : Stop Stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
    
@Client.on_callback_query(filters.regex("close_data"))
async def closedata(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbstart"))
async def started(_, query: CallbackQuery):
        buttons = [[
            InlineKeyboardButton("โ Add me to your Group โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],[
            InlineKeyboardButton("โ Basic Guide", callback_data="cbhowtouse"),
            InlineKeyboardButton("๐ Commands", callback_data="cbcmds")
            ],[
            InlineKeyboardButton('โค๏ธ Donate', url='https://t.me/DKBOTZHELP')
            ],[
            InlineKeyboardButton("๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}")
            ],[
            InlineKeyboardButton("๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
            InlineKeyboardButton("๐น Tutorial Video", url=f"{VIDEO_LINK}")
            ],[
            InlineKeyboardButton('โฆ Close the Menu โซ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=False,
            reply_markup=reply_markup,
            parse_mode='html'
        )
