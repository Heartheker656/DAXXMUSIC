from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ",              
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✭ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✭",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ ɢʀᴏᴜᴘ ✭", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ source ✮", url=f"https://github.com/Heartheker656/DAXXMUSIC"
            )
        ]
     ]
    return buttons
