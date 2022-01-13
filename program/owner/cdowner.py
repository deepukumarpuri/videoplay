
from script import Script as script
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Chat, Message
from config import *
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid




@Client.on_callback_query(filters.regex("cbbasics"))
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
» /vc - Get Your Group VC Link (Only For Public group)
» /tts - Reply The Text To Bot Convert in Voice ( Support All Language)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmins"))
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
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudos"))
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
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbowners"))
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
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )

@Client.on_callback_query(filters.regex("dkvideo"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🛡 **Here is All Tutorial Video Of This Bot** 🛡

📮 How To Play Video in VC Part 1 - {VIDEO_LINK}

🎦 Video Details :- ✨ In This Video I Tell You How To Add Bot And Userbot in Group\n.How To ⏸ Pause, ▶️ Resume, 🔇 Mute, 🔊 Unmute, ⏹ Stop, ⏩ Skip And How To Control Song/Video Volume ✨

⚡️ Tutorial Video Link :- IN HINDI :- {VIDEO_LINK} IN ENGLISH :- {EN_VIDEO_LINK}

❤️ Like This 🎦 Video And Subscrbie My Channel

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )