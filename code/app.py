from telegram.ext import ApplicationBuilder

from .config import TOKEN
from .handlers import conversation_handler

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(conversation_handler)
