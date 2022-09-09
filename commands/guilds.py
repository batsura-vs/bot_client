from shared import clear


class Guilds:
    command = "guilds"

    def __init__(self, bot):
        self.bot = bot

    def fetch_guilds(self):
        clear()
        print(f"#{self.command}")
        print("Guilds:")
        z = 1
        for i in self.bot.guilds:
            print(f"\n{z}.{i.name} [{i.member_count}] - {i.id}")
            z += 1

    async def call(self, command):
        self.fetch_guilds()
