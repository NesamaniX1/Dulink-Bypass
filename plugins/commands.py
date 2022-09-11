
from translation import *
from config import WELCOME_IMAGE
from pyrogram import Client, filters
from pyrogram.types import Message
import logging
logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start') & filters.private & filters.incoming)
async def start(c:Client, m:Message):
    if WELCOME_IMAGE:
        t = START_MESSAGE.format(m.from_user.mention)
        return await m.reply_photo(photo=WELCOME_IMAGE, caption=t)
    else:
        t = START_MESSAGE.format(m.from_user.mention)
        await m.reply_text(t, disable_web_page_preview=True)

