import pyromod.listen
import sys

from pyrogram import Client, enums

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FshubBot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            me = await self.get_me()
            self.username = me.username
            self.namebot = me.first_name

            self.LOGGER(__name__).info(
                f"✅ BOT AKTIF\nNama: {self.namebot}\nUsername: @{self.username}"
            )

        except Exception as e:
            self.LOGGER(__name__).error(f"❌ Gagal start bot: {e}")
            sys.exit()

        # 🔒 FORCE SUB CHANNEL
        if FORCE_SUB_CHANNEL:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNEL)
                link = info.invite_link

                if not link:
                    link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)

                self.invitelink = link

                self.LOGGER(__name__).info(
                    f"📢 Force Sub Channel: {info.title} ({info.id})"
                )

            except Exception as e:
                self.LOGGER(__name__).error(
                    f"❌ Gagal akses FORCE_SUB_CHANNEL: {e}"
                )
                sys.exit()

        # 🔒 FORCE SUB GROUP
        if FORCE_SUB_GROUP:
            try:
                info = await self.get_chat(FORCE_SUB_GROUP)
                link = info.invite_link

                if not link:
                    link = await self.export_chat_invite_link(FORCE_SUB_GROUP)

                self.invitelink2 = link

                self.LOGGER(__name__).info(
                    f"👥 Force Sub Group: {info.title} ({info.id})"
                )

            except Exception as e:
                self.LOGGER(__name__).error(
                    f"❌ Gagal akses FORCE_SUB_GROUP: {e}"
                )
                sys.exit()

        # 📦 DATABASE CHANNEL
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel

            test = await self.send_message(
                chat_id=db_channel.id,
                text="✅ Bot Connected",
                disable_notification=True,
            )
            await test.delete()

            self.LOGGER(__name__).info(
                f"📁 Database Channel: {db_channel.title} ({db_channel.id})"
            )

        except Exception as e:
            self.LOGGER(__name__).error(
                f"❌ Gagal akses CHANNEL_ID: {e}"
            )
            sys.exit()

        self.set_parse_mode(enums.ParseMode.HTML)

        self.LOGGER(__name__).info(
            f"🔥 BOT SIAP DIGUNAKAN 🔥\nOwner: @{OWNER}"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("🛑 Bot stopped.")
