import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8989576551:AAHuzIOeOV2PpeWUxgTDcP83CT3NCSkef2M"
ADMIN_ID = 123456789  # استبدل هذا الرقم بـ ID حسابك من @userinfobot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    greeting = f"أهلاً بك {user_first_name}! مرحباً بك في بوت التواصل الخاص بـ ROFOX. أرسل رسالتك وسأقوم بتوصيلها فوراً."
    await update.message.reply_text(greeting)

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message_text = update.message.text
    
    text_for_admin = f"📩 رسالة جديدة من {user.first_name} (@{user.username or 'بدون معرف'}):\n\n{message_text}"
    await context.bot.send_message(chat_id=ADMIN_ID, text=text_for_admin)
    
    await update.message.reply_text("تمت إرسال رسالتك بنجاح! سنرد عليك في أقرب وقت.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    app.run_polling()
  
