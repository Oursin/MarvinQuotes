import discord
import random

client = discord.Client()

quotes = ["The build failed, your project could not be tested.",
          "Test failed, invalid output.",
          "Task01 : FAILURE",
          "# Got:\n\n# But expected:\n^?ELF^B^A^A^@^@^@^@^@^@^@^@^@^C^@>^@^A^@^@^@M-p^F^@^@^@^@^@^@@^@^@^@^@^@^@^@M-^X^"
          "T^@^@^@^@^@^@^@^@^@^@@^@8^@^G^@@^@#^@",
          "L2 rule has been violated 84 times: bad indentation on start of a line",
          "Functions used but not allowed: printf",
          "implicit_L001 rule has been violated 107 times: trailing space",
          "Timed out after 30s"]

@client.event
async def on_message(message):
    if message.startswith("!marvin"):
        quote = random.choice(quotes)
        client.send_message(message.channel, quote)


client.run("MzcwNjMyODM0NjkzNzI2MjA5.DMp6ag._eKRxgLp4KmU7D-qEEGkyVcuKwA")
