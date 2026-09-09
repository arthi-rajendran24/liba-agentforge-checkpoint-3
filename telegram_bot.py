from __future__ import annotations

import json
import os

from agentforge.channel import handle_text
from agentforge.evidence import extract_image
from agentforge.service import answer


async def text_message(update, _context) -> None:
    try:
        result = handle_text(update.message.text, answer, live=True)
        await update.message.reply_text(json.dumps(result, indent=2))
    except (TypeError, ValueError, RuntimeError) as exc:
        await update.message.reply_text(f"Could not run agent: {exc}")


async def image_message(update, context) -> None:
    try:
        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        data = bytes(await file.download_as_bytearray())
        extracted = extract_image(data, "image/jpeg")
        await update.message.reply_text(
            f"EXTRACTED BUT NOT SAVED:\n{extracted}\n\nReview and approve this in the local interface before memory changes."
        )
    except (IndexError, TypeError, ValueError, RuntimeError) as exc:
        await update.message.reply_text(f"Could not review image: {exc}")


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")
    from telegram.ext import Application, MessageHandler, filters

    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))
    application.add_handler(MessageHandler(filters.PHOTO, image_message))
    application.run_polling()


if __name__ == "__main__":
    main()
