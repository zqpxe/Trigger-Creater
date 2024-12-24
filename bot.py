import discord 

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext import commands, tasks
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")

picture = "" # Picture for your bot

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"{len(synced)} Slash Commands are available")
    await bot.change_presence(activity=discord.Game(name="Trigger Creater")) 

@bot.tree.command(name="createtrigger", description="Creates a trigger from your parameters (eventlogger)")
async def createtrigger(interaction: discord.Interaction, parem1: str, parem2: str):
    cleaned_parem2 = parem2.strip('[]')
    try:
        if ',' in cleaned_parem2:
            values = ','.join(value.strip() for value in cleaned_parem2.split(','))
            trigger = f"TriggerServerEvent('{parem1.strip('[]\"')}', {values})"
        else:
            numeric_value = float(cleaned_parem2)
            if numeric_value.is_integer():
                numeric_value = int(numeric_value)
                trigger = f"TriggerServerEvent('{parem1.strip('[]\"')}', {numeric_value})"
            else:
                trigger = f"TriggerServerEvent('{parem1.strip('[]\"')}', {numeric_value})"
    except ValueError:
        trigger = f"TriggerServerEvent('{parem1.strip('[]\"')}', '{cleaned_parem2}')"

    e = discord.Embed(title="Trigger Creator", color=0xadd8e6) # https://htmlcolorcodes.com/color-names/ - I made this light blue
    e.set_thumbnail(url=picture)  # Thumbnail
    e.set_footer(text="Trigger Creator", icon_url=picture)  # Footer
    e.add_field(name="**Trigger**", value=f"```lua\n{trigger}```", inline=False)
    e.add_field(name="", value="Here is your returned trigger, which you can use!", inline=False)
    e.add_field(name="**Looped Version**", value=f"""```lua
CreateThread(function()
    for i = 1, 10 do 
        {trigger}
    end
end)
```""", inline=False)
    await interaction.response.send_message(content="", embed=e)

bot.run('') 