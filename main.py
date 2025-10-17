# main.py
import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ DÜZGÜN INTENT AYARLARI
intents = discord.Intents.default()
intents.message_content = True  # Bu izin Discord'ta AÇILMALI!
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

start_time = time.time()

GUILD_ID = 1414223132235137047
VOICE_CHANNEL_ID = 1428756795240742952

services = {
    "üyeler": ["Discord Üye", "Telegram Üye"],
    "beğeniler": [
        "YouTube Beğeni", "TikTok Beğeni", "Instagram Beğeni",
        "Facebook Beğeni", "Twitter Beğeni", "Telegram Beğeni"
    ],
    "yorumlar": [
        "YouTube Yorum", "TikTok Yorum", "Instagram Yorum",
        "Facebook Yorum", "Twitter Yorum", "Telegram Mesaj"
    ],
    "kaydetmeler": ["TikTok Kaydetme", "Instagram Kaydetme"],
    "paylaşımlar": ["TikTok Paylaşım", "Instagram Paylaşım"],
    "izlenmeler": [
        "YouTube İzlenme", "Instagram İzlenme", "TikTok İzlenme",
        "Facebook İzlenme", "Twitter İzlenme", "Telegram İzlenme",
        "Kick İzlenme", "Twitch İzlenme"
    ],
    "hesaplar": [
        "Instagram Hesap", "TikTok Hesap", "YouTube Hesap",
        "Twitter Hesap", "Facebook Hesap", "Discord Hesap",
        "Twitch Hesap", "Kick Hesap"
    ],
    "boost": [
        "Discord 24X Boost", "Discord 14X Boost", "Discord 12X Boost",
        "Discord 10X Boost", "Discord 8X Boost", "Discord 4X Boost",
        "Discord 2X Boost"
    ]
}

# Yardım
@bot.command(name="yardım")
async def yardim(ctx):
    embed = discord.Embed(
        title="🤖 LOOTUM Bot Yardım Menüsü",
        description="Aşağıdaki komutlarla tüm hizmetlere ulaşabilirsin!",
        color=0x667eea
    )
    embed.add_field(name="!hizmetler", value="Tüm kategorileri gösterir", inline=False)
    for cat in services:
        embed.add_field(name=f"!{cat}", value=f"{cat.capitalize()} hizmetlerini listeler", inline=True)
    embed.add_field(name="!uptime", value="Bot ne kadar süredir çalışıyor?", inline=False)
    embed.set_footer(text="LOOTUM • Premium Kalite • Anında Teslimat")
    await ctx.send(embed=embed)

# Hizmetler
@bot.command(name="hizmetler")
async def hizmetler(ctx):
    embed = discord.Embed(title="📦 LOOTUM Hizmet Kategorileri", color=0xff6b6b)
    for category in services:
        embed.add_field(name=category.capitalize(), value=f"`!{category}`", inline=True)
    embed.set_footer(text="Stok: Sınırsız ✅")
    await ctx.send(embed=embed)

# 🛠️ HER KATEGORİ İÇİN AYRI KOMUT (Closure hatasını önlemek için)
def create_command(category_name, items_list):
    @bot.command(name=category_name)
    async def cmd(ctx):
        embed = discord.Embed(
            title=f"🔹 {category_name.capitalize()} Hizmetleri",
            description="**Stok: Sınırsız** ✅\nFiyatlar için web sitemizi ziyaret edin.",
            color=0x4ecdc4
        )
        for item in items_list:
            embed.add_field(name=item, value="Stok: **Sınırsız**", inline=False)
        embed.set_footer(text="LOOTUM • 7/24 Destek")
        await ctx.send(embed=embed)
    return cmd

# Komutları oluştur
for cat, items in services.items():
    create_command(cat, items)

# Uptime
@bot.command(name="uptime")
async def uptime(ctx):
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    await ctx.send(
        f"🕗 **LOOTUM Bot** şu süredir aktif:\n"
        f"**{days} gün, {hours} saat, {minutes} dakika, {seconds} saniye**"
    )

# AFK ses kanalına bağlan
@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı!")
    print("🚀 LOOTUM Bot aktif ve çalışıyor!")
    guild = bot.get_guild(GUILD_ID)
    if guild:
        voice_channel = guild.get_channel(VOICE_CHANNEL_ID)
        if voice_channel:
            await voice_channel.connect()
            print(f"🔊 AFK ses kanalına bağlanıldı: {voice_channel.name}")
        else:
            print("❌ Ses kanalı bulunamadı!")
    else:
        print("❌ Sunucu bulunamadı!")

# Token
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ .env dosyasında DISCORD_TOKEN tanımlanmamış!")

bot.run(TOKEN)
