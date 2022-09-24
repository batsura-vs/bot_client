from listener import Listener
from shared import clear


class Help:
    command = "help"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        clear()
        print(f"Bot name: {self.bot.user.name}")
        for i in Listener.commands:
            print(i.command)
