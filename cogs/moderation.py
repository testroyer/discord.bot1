import discord                      # Importig packs
from discord.ext import commands    #

class Moderation(commands.Cog):

    def __init__(self , client):
        self.client = client
    
    @commands.command()
    @commands.has_role("Admin")
    async def kick(self , ctx, member : discord.Member, * , reason = None):
        await member.kick(reason = reason)

    @commands.command()
    @commands.has_role("Admin")
    async def ban(self , ctx, member : discord.Member, * , reason = None):
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member}")

    @commands.command()
    async def unban(self , ctx , * , member):
        bannedUsers = await ctx.guild.bans()
        memberName , memberDiscriminator = member.split("#")
        for ban_entry in bannedUsers:
            user = ban_entry.user
            if (user.name , user.discriminator) == (memberName , memberDiscriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {member}")
                return

    @commands.command()
    @commands.has_role("Admin")
    async def giverole(self , ctx , role: discord.Role , user :discord.Member):
        await user.add_roles(role)

    @commands.command()
    @commands.has_role("Admin")
    async def takerole(self , ctx , role: discord.Role , user :discord.Member):
        await user.remove_roles(role)

def setup(client):
    client.add_cog(Moderation(client))