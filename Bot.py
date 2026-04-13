import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ---------- НАСТРОЙКИ (ЗАМЕНИ НА СВОИ) ----------
BOT_TOKEN = "8757443610:AAF8eLvL7jPrCrSYmukKP939E64A8sp6eLo"  # Токен от BotFather
REF_ID = "https://pornworks.app/?refid=fantasy-prompt-bot_onrender_com"  # Твой реферальный код (цифры после ?ref= в ссылке)
# ------------------------------------------------

# Логирование (чтобы видеть ошибки)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# База тегов (та же, что в предыдущем генераторе)
fantasy_data = {
    "races": ["elf", "dark elf", "orc female", "demoness", "succubus", "tiefling", "goblin girl",
              "vampire lady", "angel", "fallen angel", "dragon kin", "kobold", "slime girl",
              "wolf girl", "cat girl", "harpy", "lamia", "centaur woman"],
    "bodies": ["muscular", "curvy", "thick thighs", "wide hips", "toned abs", "small breasts",
               "huge breasts", "petite", "tall", "athletic", "plump", "pregnant", "sweat",
               "oiled skin", "visible veins", "soft skin", "scarred body", "tattooed"],
    "faces": ["angry", "blush", "smirk", "ahegao", "serious", "looking at viewer",
              "closed eyes", "teary eyes", "evil grin", "licking lips", "open mouth"],
    "outfits": ["leather armor", "torn dress", "see through silk robe", "dark plate armor",
                "tribal fur", "battle worn bikini", "chains only", "nothing", "slime covered",
                "transparent cloth", "ripped stockings", "high heels", "elven jewelry"],
    "actions": ["fighting a monster", "casting dark magic", "bound by tentacles", "riding a dragon",
                "kneeling", "spread legs", "from behind", "arms above head", "dominating a throne",
                "bathing in moonlit pond", "chained to an altar", "holding a glowing sword",
                "surrendering", "casting healing spell", "drinking potion"],
    "backgrounds": ["dark dungeon", "forbidden forest", "volcanic cave", "ancient elven ruins",
                    "demon lord's castle", "enchanted glade", "floating islands", "underwater temple",
                    "wizard's tower", "frosty mountains", "haunted graveyard"],
    "effects": ["sweat", "glowing runes", "magic particles", "wet skin", "steam",
                "moonlight", "fire sparks", "blood splatter", "shadow tentacles", "ethereal glow"],
    "lighting": ["cinematic lighting", "volumetric fog", "rim light", "harsh shadows",
                 "soft candle light", "bioluminescence", "lightning flash", "dusk"]
}

def generate_prompt():
    race = random.choice(fantasy_data["races"])
    body = random.choice(fantasy_data["bodies"])
    face = random.choice(fantasy_data["faces"])
    outfit = random.choice(fantasy_data["outfits"])
    action = random.choice(fantasy_data["actions"])
    bg = random.choice(fantasy_data["backgrounds"])
    effect = random.choice(fantasy_data["effects"])
    light = random.choice(fantasy_data["lighting"])
    
    prompt = (f"{race}, {body}, {face}, wearing {outfit}, {action}, {bg}, {effect}, {light}, "
              f"masterpiece, best quality, nsfw, cgi, intricate details")
    return prompt

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 *Hardcore Fantasy Prompt Bot* 🔥\n\n"
        "Я генерирую случайные промпты для PornWorks AI (стиль Hardcore Fantasy).\n\n"
        "Команды:\n"
        "/prompt — получить один промпт\n"
        "/link — твоя реферальная ссылка для генерации\n\n"
        "Скопируй промпт, перейди по ссылке и вставь его в поле на сайте!",
        parse_mode="Markdown"
    )

# Команда /prompt
async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    p = generate_prompt()
    await update.message.reply_text(f"🎲 *Твой промпт:*\n\n`{p}`", parse_mode="Markdown")

# Команда /link
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref_link = f"https://pornworks.app/?ref={REF_ID}"
    await update.message.reply_text(
        f"🔗 *Твоя реферальная ссылка:*\n{ref_link}\n\n"
        f"Перейди по ней, зарегистрируйся и вставляй промпты из бота в поле генерации.",
        parse_mode="Markdown"
    )

# Запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prompt", prompt))
    app.add_handler(CommandHandler("link", link))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
