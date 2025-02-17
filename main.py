import discord
import os
from dotenv import load_dotenv
import google.generativeai as genai
from chat_loader import load_chat_context

load_dotenv()

my_secret = os.environ['TOKEN']
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)
       
initial_history = load_chat_context()
chat_session = model.start_chat(history=initial_history)

# chat_session = model.start_chat(
#   history=[
#   ]
# )

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
                clean_content = message.content.replace(self.user.mention, '').strip()

                if not clean_content:
                    await message.channel.send("Hello! How can I assist you?")
                    return
                
                response = chat_session.send_message(clean_content)
                channel  = message.channel
                await channel.send(response.text)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(my_secret)
