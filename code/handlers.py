import logging

from telegram import Update
from telegram.ext import (
    CommandHandler, ContextTypes, ConversationHandler, filters, MessageHandler,
)
from tortoise.exceptions import ValidationError

from .config import ANQAU_USER_ID
from .models import Review

logger = logging.getLogger()


class State:
    SUBMIT = 'submit'


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет, ты можешь оставить здесь любое анонимное сообщение\n\n(или напиши /cancel для отмены)')  # noqa: E501
    return State.SUBMIT


async def submit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        review = await Review.create(text=update.message.text)
    except ValidationError:
        await update.message.reply_text('Твое сообщение слишком длинное. Попробуй еще раз')  # noqa: E501

    logger.info(f'Review saved: "{review.text}"')
    await update.message.reply_text('Твое сообщение получено. Спасибо за вовлеченность!\n\n(напиши /start для отправки нового сообщения)')  # noqa: E501
    await context.bot.send_message(ANQAU_USER_ID, f'Получено новое сообщение: "{update.message.text}"')  # noqa: E501
    return ConversationHandler.END


async def cancel_handler(update, context):
    return ConversationHandler.END


conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start_handler),
    ],
    states={
        State.SUBMIT: [
            CommandHandler('cancel', cancel_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), submit_handler),
        ],
    },
    fallbacks=[
        CommandHandler('cancel', cancel_handler),
    ],
)
