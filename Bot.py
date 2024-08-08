import discord
import openai
import os
import traceback
import re
import configparser
from discord.ext import commands, tasks
from discord import app_commands
from collections import deque

# Load configuration from config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')

OPENAI_API_KEY = config.get('DEFAULT', 'OPENAI_API_KEY')
ASSISTANT_ID = config.get('DEFAULT', 'ASSISTANT_ID')
DISCORD_BOT_TOKEN = config.get('DEFAULT', 'DISCORD_BOT_TOKEN')

if not DISCORD_BOT_TOKEN or not OPENAI_API_KEY or not ASSISTANT_ID:
    raise ValueError("Required environment variables are not set.")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
        self.queue = deque()
        self.processing = False

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        print(f'Bot is connected to the following guilds:')
        for guild in self.guilds:
            print(f' - {guild.name} (id: {guild.id})')
        self.process_queue.start()

    @tasks.loop(seconds=1)
    async def process_queue(self):
        if self.queue and not self.processing:
            self.processing = True
            interaction, question = self.queue.popleft()
            await self.handle_askpkp(interaction, question)
            self.processing = False

    async def handle_askpkp(self, interaction, question):
        try:
            openai.api_key = OPENAI_API_KEY 
            # Use the OpenAI client to create a thread and send the question
            print("Creating thread...")
            client = openai.OpenAI(api_key=openai.api_key)
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=f"Answer the following question: {question}"
            )
            print(f"Message sent to thread {thread.id}")

            # Poll the run to get the assistant's response
            print("Polling run...")
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=ASSISTANT_ID,
                instructions="Du bist ein Experte der Polnischen Eisenbahn und des Simulators Train Driver 2 sowie Simrail. Beantworte die gestellten Fragen fachlich und kompakt. Gib keine Quellen oder Referenzen in deiner Antwort an."
            )
            print(f"Run response: {run}")

            if run.status == 'completed':
                print("Run completed, retrieving messages...")
                messages = client.beta.threads.messages.list(thread_id=thread.id)
                # Access the list of messages in the `messages` object
                message_data = messages.data
                if message_data:
                    last_message = message_data[0]
                    if last_message.content:
                        # Access the TextContentBlock object and extract text from it
                        text_content_block = last_message.content[0]
                        response_text = text_content_block.text.value.strip()

                        # Remove references from the response text
                        response_text = re.sub(r'【\d+:\d+†[^】]+】', '', response_text)
                    else:
                        response_text = "No content found in the last message"
                else:
                    response_text = "No messages found"
            else:
                response_text = f"An error occurred: {run.status}"

            # Send the response back to the Discord channel
            await interaction.followup.send(response_text)

        except Exception as e:
            # Send the error message back to the Discord channel
            await interaction.followup.send(f"An error occurred: {str(e)}")
            print(f"An error occurred: {str(e)}")
            traceback.print_exc()

bot = MyBot()

@bot.tree.command(name="askpkp", description="Ask a question to the PKP Expert")
async def askpkp(interaction: discord.Interaction, question: str):
    print(f"Received question from {interaction.user}: {question}")

    await interaction.response.defer()  # Defer the response to avoid timeout
    bot.queue.append((interaction, question))

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
