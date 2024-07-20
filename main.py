import discord
import os
import requests
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Set up bot intents to receive specific types of events
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    user_id = str(message.author.id)


    # Respond to a hello command
    if message.content == '$hello':
        await message.channel.send(f"Hello there <@{message.author.id}>! How may I assist you?")
    else:
        await bot.process_commands(message)


def download_shutterstock_video(category,asset_id):
    try:
      url_template = f"https://stock.adobe.com/search?k={category}&asset_id={asset_id}"

    except Exception as err:
        return f"An error occurred: {err}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url_template, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    video_containers = soup.find_all('div', class_='js-video-result-container')

    if video_containers:
        first_video = video_containers[0]
        video_thumb_container = first_video.find('div', class_='js-video-thumb-container')
        if video_thumb_container and 'data-src' in video_thumb_container.attrs:
            video_url = video_thumb_container['data-src']
            download=requests.get(video_url,headers=headers)
            if download.status_code == 200:
                # Proceed with download
                with open("video.mp4", "wb") as f:
                    for chunk in download.iter_content(chunk_size=1024):
                      f.write(chunk)
                return "video.mp4"
            else:
                return f"Error downloading video. Status code: {download.status_code}"


        else:
            return "Could not find video URL in the container."
    else:
        return "No video containers found."



@bot.command()
async def download(ctx, asset_id: int, category: str = None):
    # Command to download a video
    await ctx.send(f"Downloading video for asset ID: {asset_id}")
    video_file = download_shutterstock_video(category, asset_id)
    if video_file and video_file.endswith('.mp4'):
        await ctx.send("Video downloaded successfully!", file=discord.File(video_file))
    else:
        await ctx.send(f"Failed to download the video. {video_file}")

try:
    bot.run(os.getenv('Token'))

except Exception as err:
    print(f"An error occurred: {err}")

