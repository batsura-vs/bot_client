from shared import clear


class Clear:
    command = "clear"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        clear()
        print('Logged in as')
        print(f"Name: {self.bot.user.name}")
        print(f"Bot id: {self.bot.user.id}")
        print(f"Guilds count: {len(self.bot.guilds)}")
        print('------')
