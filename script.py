class Script(object):
    START_TXT = """ โจ Welcome {}, 

๐ญ <a href=https://t.me/VC_VIDEO_PLAY_BOT>VC VIDEO PLAY BOT</a>! \nAllows You To Play Music And Video On Groups Through The New Telegram's Video Chats!

๐ก Find Out All The Bot's Commands And How They Work By Clicking On The ยป ๐ Commands Button!

๐ To Know How to Use This Bot, Please Click On The ยป โ Basic Guide button!\n\n You Can Also Watch This Tutorial Video\n In English Voice :- https://youtu.be/dEqGW8Ir8zY \n In Hindi Voice :- https://youtu.be/WegxZFKPZeI """

    GROUP_START_TXT = """ Hello {}, 

My name is <a href=https://t.me/hhh>bhh</a>!

I Am Most Powerful VC VIDEO PLAY BOT Use Me To Play Song/Video in VC

๐ If You Don't Know How To Use Me Watch This Video ๐\nIn English Voice :- https://youtu.be/dEqGW8Ir8zY \n In Hindi Voice :- https://youtu.be/WegxZFKPZeI """

    VC_TXT = """Hello {},

My name is <a href=https://t.me/VC_VIDEO_PLAY_BOT>VC VIDEO PLAY BOT</a>!

This Command For Group Add Me To Your With Click Below Button

๐ If You Don't Know How To Use Me Watch This Video ๐\nIn English Voice :- https://youtu.be/dEqGW8Ir8zY \n In Hindi Voice :- https://youtu.be/WegxZFKPZeI """

    G_VC_TXT = """ Hi {} ๐๏ธ! 


             ๐๏ธ  Voice Chat Link ๐๏ธ
____________________------------______________________

๐๏ธ [Here Is Your Voice Chat Link](https://t.me/{}?voicechat) ๐๏ธ
____________________------------______________________


Enjoy ๐๏ธโค๏ธ!"""


    HELP_TXT = """ โจ Hi {}, 

Here is the Help Menu For This Bot ๐!

"""



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
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """โYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """๐ฎ Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """โI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
