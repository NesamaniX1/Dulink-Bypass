from pyrogram import Client, filters
from utils import main_convertor_handler, extract_link
from pyrogram.types import Message
import logging
from pyrogram.types import Message
logger = logging.getLogger(__name__)


# Private Chat
@Client.on_message(filters.private & filters.incoming)
async def private_link_handler(c: Client, message: Message):
    if message.text and message.text.startswith('/'):
        return
    if not message.text and not message.caption and not message.reply_markup:
        return
    if message.text:
        caption = message.text.html
    elif message.caption:
        caption = message.caption.html
    if len(await extract_link(caption)) <= 0 and not message.reply_markup:
        return
    try:
        txt = await message.reply('`Cooking... It will take some time`', quote=True)
        await main_convertor_handler(message)
    except Exception as e:
        await message.reply(f"Error while trying to convert links {e}:", quote=True)
        logger.exception(e)
    finally:
        await txt.delete()

