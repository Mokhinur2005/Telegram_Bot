from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

import os

TOKEN = os.getenv("7670094408:AAGgn1tFG2TIBFWcdTBE4hMe3esbIY-yBPI")  # Railway-ga qo'shiladigan token

CHANNELS = ["@Botirali_Zokirovich_blog", "@Murodova_Mohinur1"]
SECRET_GROUP = "https://t.me/+gV4MePhUXKgxZjJi"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def check_subscription_keyboard():
    keyboard = InlineKeyboardMarkup()
    for channel in CHANNELS:
        btn = InlineKeyboardButton("➕ Kanalga qo'shilish", url=f"https://t.me/{channel[1:]}")
        keyboard.add(btn)
    keyboard.add(InlineKeyboardButton("✅ Tekshirish", callback_data="check_subs"))
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("📢 Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling!", reply_markup=check_subscription_keyboard())

@dp.callback_query_handler(lambda c: c.data == 'check_subs')
async def check_subscriptions(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    for channel in CHANNELS:
        chat_member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        if chat_member.status not in ["member", "administrator", "creator"]:
            await callback_query.answer("❌ Hali hamma kanallarga a'zo bo'lmadingiz!", show_alert=True)
            return
    
    await bot.send_message(user_id, "✅ Rahmat! Endi ro'yxatdan o'tish uchun F.I.Sh ni kiriting:")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
