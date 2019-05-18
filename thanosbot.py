import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('All Praise The Duckling!'):
        await message.channel.send('ALL')
        await message.channel.send('PRAISE')
        await message.channel.send('THE')
        await message.channel.send('DUCKLING!')

    if message.content.startswith('$d20'):
        roll = random.randint(1,20)
        if roll == 20:
            await message.channel.send("You rolled a 20")
        elif roll == 19:
            await message.channel.send("You rolled a 19; Soeexhinf day is celebrated on the 19th.")
        elif roll == 18:
            await message.channel.send("You rolled an 18")
        elif roll == 17:
            await message.channel.send("You rolled a 17")
        elif roll == 16:
            await message.channel.send("You rolled a 16")
        elif roll == 15:
            await message.channel.send("You rolled a 15; the minimum duration of a Splatobatics match in minutes.")
        elif roll == 14:
            await message.channel.send("You rolled a 14")
        elif roll == 13:
            await message.channel.send("You rolled a 13")
        elif roll == 12:
            await message.channel.send("You rolled a 12; the number of light gods.")
        elif roll == 11:
            await message.channel.send("You rolled an 11")
        elif roll == 10:
            await message.channel.send("You rolled a 10; the number of types of Splatobatics ink.")
        elif roll == 9:
            await message.channel.send("You rolled a 9")
        elif roll == 8:
            await message.channel.send("You rolled an 8; this is the amount of individual Purple territories, including the island colonies. ")
        elif roll == 7:
            await message.channel.send("You rolled a 7")
        elif roll == 6:
            await message.channel.send("You rolled a 6")
        elif roll == 5:
            await message.channel.send("You rolled a 5; this is said to be Mauve's favorite number.")
        elif roll == 4:
            await message.channel.send("You rolled a 4; may the 4th be with you (Space Imperium ftw).")
        elif roll == 3:
            await message.channel.send("You rolled a 3; fun fact, there were 3 major Purple kingdoms before the Imperium was formed.")
        elif roll == 2:
            await message.channel.send("You rolled a 2; there are only 2 Purple gods created by Mythiie himself.")
        elif roll == 1:
            await message.channel.send("You rolled a 1; Purpureus has forsaken you.")
        else:
            await message.channel.send(roll)
    if message.content.startswith('$disappointing'):
        await message.channel.send('https://i.redd.it/3xfzbmjla7u11.jpg')

    if message.content.startswith('$simple'):
        await message.channel.send('https://i.redd.it/gw58fxltkyn21.png')

    if message.content.startswith('$snap'):
        await message.channel.send('https://tenor.com/view/thanos-finger-snap-disappear-gif-13174976')

    if message.content.startswith('$soeexhinf'):
        await message.channel.send('soeexhinf')

    if message.content.startswith('$sorry'):
        await message.channel.send('https://i.redd.it/691ytkh6kyn21.png')

    if message.content.startswith('$thanosecar'):
        await message.channel.send('https://i.redd.it/aguv5r16czg21.png')

    if message.content.startswith('$whateveriwant'):
        await message.channel.send('https://i.redd.it/rlw96h5qlyn21.png')


        
client.run('NTc5MTA4NjUwNjk4OTMyMjM0.XN9Y9Q.9vtyQkGZOAtpBa0m1-gEbFTcQB4')
