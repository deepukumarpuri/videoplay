class Script(object):
    START_TXT = """✨ Welcome {},

💭 <a href=https://t.me/VC_VIDEO_PLAY_BOT>VC VIDEO PLAY BOT</a>! **Allows you to play music and video on groups through the new Telegram's video chats!**

**💡 Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**

**🔖 To know how to use this bot, please click on the » ❓ Basic Guide button!**\n\n You Can Also Watch This Tutorial Video\n In English Voice :- \n In Hindi Voice :- """

    GROUP_START_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

I Am Most Powerful VC VIDEO PLAY BOT Use Me To Play Song/Video in VC

🔆 If You Don't Know How To Use Me Watch This Video 🔆\nIn English Voice :- \n In Hindi Voice :- """

    VC_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

This Command For Group Add Me To Your With Click Below Button

🔆 If You Don't Know How To Use Me Watch This Video 🔆\nIn English Voice :- \n In Hindi Voice :-  """

    G_VC_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..</b>"""





    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""



    LOG_TEXT_G = """#New_Group
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#New_User
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
