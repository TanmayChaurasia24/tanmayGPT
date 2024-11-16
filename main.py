

import discord
import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

openaitoken = os.getenv('openaitoken')

my_secret = os.getenv('token')

print(openaitoken)
print(token)

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=message.content,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "text"})
        messagetosend = response.choices[0].message.content
        channel = message.channel
        await channel.send(messagetosend)
        await channel.send("sending message hello")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(my_secret)
