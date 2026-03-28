import os
import random
import asyncio
import schedule
import time
from telegram import Bot

# --- KONFIGURACE (NASTAVENÍ) ---
# POZNÁMKA: Na GitHubu necháváme tyto hodnoty prázdné z bezpečnostních důvodů.
# V lokálním prostředí se tyto údaje načítají z proměnných prostředí (.env).
TOKEN = "ZDE_VLOZTE_VAS_TELEGRAM_TOKEN" 
NATALKA_ID = 000000000  # ID příjemce
MOJE_ID = 000000000     # ID odesílatele pro potvrzení

# --- SEZNAM ZPRÁV ---
SEZNAM_ZPRAV = [
    "Ahoj lásko, chci ti jen popřát hezký den a říct ti, že tě miluju. ❤️",
    "Ahoj krásko, moc mi chybíš a myslím na tebe. ✨",
    "Ahoj kočičko, dneska ti to určitě sluší a nemůžu se dočkat, až tě uvidím. 🌸",
    "Dobré ráno, miláčku! Doufám, že se dneska vyspíš do růžova. ☀️",
    "Krásný den přeju! Myslím na tebe a posílám pusu. 💋",
    "Ahoj sluníčko, věřím, že dnešek zvládneš levou zadní! 🥰"
]

async def posli_vsem():
    """Funkce pro výběr náhodné zprávy a její odeslání přes Telegram API."""
    bot = Bot(token=TOKEN)
    vybrana_zprava = random.choice(SEZNAM_ZPRAV)
    
    try:
        # 1. Odeslání zprávy příjemci
        await bot.send_message(chat_id=NATALKA_ID, text=vybrana_zprava)
        
        # 2. Potvrzení odesílateli
        potvrzeni = f"✅ Hotovo! Odesláno: '{vybrana_zprava}'"
        await bot.send_message(chat_id=MOJE_ID, text=potvrzeni)
        print(potvrzeni)

    except Exception as e:
        print(f"❌ Chyba při odesílání: {e}")

def naplanuj():
    """Nastavení časovače pro každodenní spouštění."""
    # Naplánování na 12:15 každý den
    schedule.every().day.at("12:15").do(lambda: asyncio.run(posli_vsem()))
    print("🚀 Bot je aktivní a čeká na nastavený čas...")

if __name__ == "__main__":
    naplanuj()
    while True:
        schedule.run_pending()
        time.sleep(1)
