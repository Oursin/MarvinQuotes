import discord
import random

client = discord.Client()


@client.event
async def on_message(message):
    ismarvin = message.content.startswith("!marvin")
    print(ismarvin)
    if ismarvin:
        quotes = ["The build failed, your project could not be tested.",
                  "Test failed, invalid output.",
                  "Task01 : FAILURE",
                  "# Got:\n\n# But expected:\n^?ELF^B^A^A^@^@^@^@^@^@^@^@^@^C^@>^@^A^@^@^@M-p^F^@^@^@^@^@^@@^@^@^@^@^@^@^@M-^X^"
                  "T^@^@^@^@^@^@^@^@^@^@@^@8^@^G^@@^@#^@",
                  "L2 rule has been violated 84 times: bad indentation on start of a line",
                  "Functions used but not allowed: printf",
                  "implicit_L001 rule has been violated 107 times: trailing space",
                  "Timed out after 30s",
                  "G1 rule has been violated 1 times: you must start your source code with a correctly formatted Epitech standard header",
                  "# Got:\n-rw-rw-r-- 1  0  test01\n-rwxrwxr-x 1 13  test02\nlrwxrwxrwx 1  6  test03 -> test02\n# But expected:\n-rw-rw-r-- 1  0  test01\n-rwxrwxr-x 1 12  test02\nlrwxrwxrwx 1  6  test03 -> test02",
                  "# Executing all tests...\n# Test crashed (SIGPIPE)",
                  "# Task file not found."]
        choice = random.choice(quotes)
        print(choice)
        await client.send_message(message.channel, choice)


client.run("MzcwNjMyODM0NjkzNzI2MjA5.DMp6ag._eKRxgLp4KmU7D-qEEGkyVcuKwA")
