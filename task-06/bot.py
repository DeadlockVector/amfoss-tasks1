import os
from dotenv import find_dotenv, load_dotenv

import discord
from discord.ext import commands

import scraper

# getting the token from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# intents apparently needed
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '/', intents = intents)   #initialising client as a bot object

@client.event
async def on_ready():
    print("We're on")     # oh yeah we're on
    print("-------")

# get the data from scraper, feed into this function
# Team1/Team2 name and score as well as match summary
# append fetched score to the csv file
@client.command()
async def livescore(ctx):
    URL = 'https://www.espncricinfo.com/live-cricket-score'
    m = scraper.getliveScore(URL)
    if (str(m)=="ESPN error" or str(m)=="No Live Matches"):
        await ctx.send(m)
    else:
        message = f'{m["team1"][0]} : Score {m["team1"][2]} | Overs {m["team1"][1]}\n{m["team2"][0]} : Score {m["team2"][2]} | Overs {m["team2"][1]}\n{m["summary"]}'
        print(message)
        await ctx.send(message)

# results of the most recent match
@client.command()
async def results(ctx):
    URL = 'https://www.espncricinfo.com/live-cricket-match-results'
    m = scraper.getResult(URL)
    message = f'Match: {m[0]}\nResult: {m[1]}'
    print(message)
    await ctx.send(message)

# send the csv file to the chat
@client.command()
async def generate(ctx):
    await ctx.send(file=discord.File(r'./task-06/info.csv'))

@client.command()
async def clearHistory(ctx):
    await ctx.send("Cleared history")
    scraper.clearCsv()

#just listing out all the commands
@client.command()
async def getHelp(ctx):
    message = "Live cricket scores for you Harigovind\nUse '/' before each command\n- /livescore: Get the real time score\n- /generate: Generate a CSV file of all fetched data\n- /clearHistory: Clear the csv file of previous entries\n- /results: Get the results of the most recent match"
    await ctx.send(message)

client.run(BOT_TOKEN)