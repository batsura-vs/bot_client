from shared import clear


class InviteBot:
    command = "invite bot"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        clear()
        print(f"https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot")
