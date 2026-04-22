from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Cek bot hidup
 └ /uptime - Status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Melihat logs bot
 ├ /setvar - Set variabel bot
 ├ /delvar - Hapus variabel bot
 ├ /getvar - Lihat variabel bot
 ├ /users - Statistik pengguna
 ├ /batch - Buat link banyak file
 ├ /speedtest - Cek kecepatan server
 └ /broadcast - Kirim pesan ke semua user

👨‍💻 Developed by </b><a href='https://t.me/slengean22'>@slengean22</a>
"""

    close = [
        [InlineKeyboardButton("❌ Tutup", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("📖 Help & Commands", callback_data="help"),
            InlineKeyboardButton("❌ Tutup", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("👤 Tentang Bot", callback_data="about"),
            InlineKeyboardButton("❌ Tutup", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot Ini:

@{} adalah Bot Telegram untuk menyimpan file / postingan dan menghasilkan link akses khusus.

 • Creator: @USERNAME_LU
 • Framework: Pyrogram
 • Version: Custom Rebuild

👨‍💻 Developed by </b><a href='https://t.me/slengean22'>@slengean22</a>
"""
