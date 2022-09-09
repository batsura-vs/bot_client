import asyncio
import re


class Listener:
    commands = []

    def add_command(self, command):
        self.commands.append(command)

    def listen(self, bot):
        while True:
            command = input().strip()
            for i in self.commands:
                if bool(re.search(i.command, command)):
                    asyncio.run_coroutine_threadsafe(i.call(command), bot.loop)
                    break
