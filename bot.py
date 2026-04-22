from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_TOKEN, CHANNEL_1, CHANNEL_2, GROUP

app = Client("fshub", bot_token=BOT_TOKEN)


# 🔍 CEK JOIN SEMUA
async def is_joined_all(client, user_id):
    try:
        ch1 = await client.get_chat_member(CHANNEL_1, user_id)
        ch2 = await client.get_chat_member(CHANNEL_2, user_id)
        grp = await client.get_chat_member(GROUP, user_id)

        return (
            ch1.status in ["member", "administrator", "creator"]
            and ch2.status in ["member", "administrator", "creator"]
            and grp.status in ["member", "administrator", "creator"]
        )
    except:
        return False


# 🚀 START
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    joined = await is_joined_all(client, user_id)

    if not joined:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Channel 1", url=f"https://t.me/{CHANNEL_1.replace('@','')}")],
            [InlineKeyboardButton("📢 Channel 2", url=f"https://t.me/{CHANNEL_2.replace('@','')}")],
            [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP.replace('@','')}")],
            [InlineKeyboardButton("✅ Coba Lagi", callback_data="check_join")]
        ])

        await message.reply_text(
            "❌ Wajib join semua dulu bro!\nKlik tombol bawah 👇",
            reply_markup=keyboard
        )
    else:
        await message.reply_text(
            "🔥 Mantap! Lu udah join semua\nAkses file kebuka 🚀"
        )


# 🔁 CEK ULANG
@app.on_callback_query(filters.regex("check_join"))
async def check_join(client, callback_query):
    user_id = callback_query.from_user.id

    joined = await is_joined_all(client, user_id)

    if joined:
        await callback_query.message.edit_text(
            "🔥 Verified! Lu udah join semua 🚀"
        )
    else:
        await callback_query.answer("❌ Masih ada yang belum lu join!", show_alert=True)


app.run()
