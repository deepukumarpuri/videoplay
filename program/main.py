
        buttons = [[
            InlineKeyboardButton("🤔 How To Use Me 🤔", callback_data="cbhowtouse")
            ],[
            InlineKeyboardButton("👷🏻 Admin Command", callback_data="cbadmin"),
            InlineKeyboardButton("📚 Basic Command", callback_data="cbbasic")
            ],[
            InlineKeyboardButton("🧙🏻 Sudo Command", callback_data="cbsudo"),
            InlineKeyboardButton("👨‍💻 Owner Command", callback_data="cbowner")
            ],[
            InlineKeyboardButton("📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
            InlineKeyboardButton("👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}")
            ],[
            InlineKeyboardButton('⌦ Close the Menu ⌫', callback_data='close_data')
        ]]
