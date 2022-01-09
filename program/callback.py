# Copyright (C) 2021 By @DKBOTZ And Some Creadit To VEEZMUSIC

from script import Script as script
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Chat, Message
from config import *
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid


@Client.on_callback_query(filters.regex("cbstarts"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Allows You To Play Music And Video On Groups Through The New Telegram's Video Chats!**

**💡 Find Out All The Bot's Commands And How They Work By Clicking On The » 📚 Commands Button!**

**🔖 To Know How to Use This Bot, Please Click On The » ❓ Basic Guide button!**\n\n You Can Also Watch This Tutorial Video\n In English Voice :- {EN_VIDEO_LINK} \n In Hindi Voice :- {VIDEO_LINK}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⌦ Close the Menu ⌫", callback_data="close_data"
                    )
                ],
            ]
        ),
        disable_web_page_preview=False,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Commands", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Commands", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Commands", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /mplay (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

» /ytthumb (Youtube Link) - Download Youtube Thumbnail Ex :- /ytthumb {EN_VIDEO_LINK}
» /vc - Get Your Group VC Link (in group)
» /tts - Reply The Text To Bot Convert in Voice ( Support All Language)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("You're An Anonymous Admin !\n\n» Revert Back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Settings Of** {query.message.chat.title}\n\n⏸ : Pause Stream\n▶️ : Resume Stream\n🔇 : Mute Userbot\n🔊 : Unmute Userbot\n⏹ : Stop Stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)

@Client.on_callback_query(filters.regex("cbowner"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❄️ Here is The Owner Commands ❄️

» /uptime - Check Bot Up Times
» /status - Check Bot Stats
» /ban_user (user id) - Ban The User
» /unban_user (user id)  - Unban The User
» /banned - Check Banned User

More Feature Coming Soon

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("dkvideo"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🛡 **Here is All Tutorial Video Of This Bot** 🛡

📮 How To Play Video in VC Part 1 - 

✨ In This Video I Tell You How To Add Bot And Userbot in Group\n.How To ⏸ Pause, ▶️ Resume, 🔇 Mute, 🔊 Unmute, ⏹ Stop, ⏩ Skip And How To Control Song/Video Volume ✨

⚡️ Tutorial Video Link :- IN HINDI :- {VIDEO_LINK} IN ENGLISH :- {EN_VIDEO_LINK}

❤️ Like This 🎦 Video And Subscrbie My Channel

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
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
            InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],[
            InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse"),
            InlineKeyboardButton("📚 Commands", callback_data="cbcmds")
            ],[
            InlineKeyboardButton('❤️ Donate', url='https://t.me/DKBOTZHELP')
            ],[
            InlineKeyboardButton("👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}")
            ],[
            InlineKeyboardButton("📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
            InlineKeyboardButton("📹 Tutorial Video", url=f"VIDEO_LINK")
            ],[
            InlineKeyboardButton('⌦ Close the Menu ⌫', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            disable_web_page_preview=False,
            reply_markup=reply_markup,
            quote=True,
            parse_mode='html'
        )