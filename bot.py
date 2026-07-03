import os
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart, Command
from keep_alive import keep_alive

# === КОНФИГУРАЦИЯ ===
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN secret is not set. Add it in Replit Secrets before starting the bot.")
MINI_APP_URL = "https://777ernest888-oss.github.io/demo-miniapp-realty/?agent=23062026-001"
REGISTER_URL = "https://777ernest888-oss.github.io/demo-miniapp-realty/register.html?agent=23062026-001"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
router = Router()

# === КЛАВИАТУРЫ ===
def welcome_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Открыть каталог", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="✍️ Стать агентом", web_app=WebAppInfo(url=REGISTER_URL))],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="main_menu")]
    ])

def help_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Каталог", callback_data="open_catalog")],
        [InlineKeyboardButton(text="✍️ Регистрация", callback_data="become_agent")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])

def catalog_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Открыть каталог", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])

def register_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Заполнить анкету", web_app=WebAppInfo(url=REGISTER_URL))],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])

def status_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Открыть Mini App", web_app=WebAppInfo(url=MINI_APP_URL))],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])

def unknown_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="main_menu")]
    ])

# === КОМАНДЫ ===
@router.message(CommandStart())
async def cmd_start(m: Message):
    text = (
        "<b>Добро пожаловать в ПРОСТОРЫ.НОВОСТРОЙКИ!</b>\n\n"
        "🚀 Современный инструмент продаж\n"
        "🎨 Персонализация под ваш бренд\n"
        "📊 Фильтры, карты, заявки в 1 клик\n"
        "📈 Увеличение конверсии до 50%\n"
        "💬 Простота и функциональность\n\n"
        "👇 <b>Вы агент и хотите продавать новостройки ПРОСТО и СОВРЕМЕННО?</b>\n"
        "Тогда регистрируйтесь и бесплатно тестируйте приложение 7 дней!\n\n"
        "✨ <b><i>ПРОСТОРЫ = Продавай + Красиво</i></b>"
    )
    await m.answer(text, reply_markup=welcome_kb(), parse_mode="HTML")

@router.message(Command("help"))
async def cmd_help(m: Message):
    text = (
        "<b>📖 Доступные команды:</b>\n\n"
        "/start — Главное меню\n"
        "/catalog — Открыть каталог объектов\n"
        "/register — Регистрация агента\n"
        "/status — Статус вашей заявки\n"
        "/help — Эта справка\n\n"
        "Или нажмите кнопки ниже 👇"
    )
    await m.answer(text, reply_markup=help_kb(), parse_mode="HTML")

@router.message(Command("catalog"))
async def cmd_catalog(m: Message):
    await m.answer("<b>🔍 Каталог новостроек</b>\n\nНажмите кнопку ниже, чтобы открыть каталог:", reply_markup=catalog_kb(), parse_mode="HTML")

@router.message(Command("register"))
async def cmd_register(m: Message):
    text = (
        "<b>✍️ Регистрация агента</b>\n\n"
        "Заполните анкету и получите бесплатный доступ на 7 дней:\n\n"
        "✅ Персональный кабинет\n"
        "✅ Доступ ко всем объектам\n"
        "✅ Заявки от клиентов в реальном времени"
    )
    await m.answer(text, reply_markup=register_kb(), parse_mode="HTML")

@router.message(Command("status"))
async def cmd_status(m: Message):
    text = (
        "<b>📊 Статус заявки</b>\n\n"
        "Для проверки статуса обратитесь к менеджеру:\n"
        "@prostors_manager\n\n"
        "Или используйте Mini App для отслеживания заявок."
    )
    await m.answer(text, reply_markup=status_kb(), parse_mode="HTML")

@router.message()
async def unknown_message(m: Message):
    text = "Неизвестная команда.\n\nНажмите /help для списка доступных команд или /start для главного меню."
    await m.answer(text, reply_markup=unknown_kb(), parse_mode="HTML")

# === CALLBACKS ===
@router.callback_query(F.data == "open_catalog")
async def cb_open_catalog(c: CallbackQuery):
    await c.message.edit_text("<b>🔍 Каталог новостроек</b>\n\nНажмите кнопку ниже, чтобы открыть каталог:", reply_markup=catalog_kb(), parse_mode="HTML")
    await c.answer()

@router.callback_query(F.data == "become_agent")
async def cb_become_agent(c: CallbackQuery):
    text = (
        "<b>✍️ Регистрация агента</b>\n\n"
        "Заполните анкету и получите бесплатный доступ на 7 дней:\n\n"
        "✅ Персональный кабинет\n"
        "✅ Доступ ко всем объектам\n"
        "✅ Заявки от клиентов в реальном времени"
    )
    await c.message.edit_text(text, reply_markup=register_kb(), parse_mode="HTML")
    await c.answer()

@router.callback_query(F.data == "main_menu")
async def cb_main_menu(c: CallbackQuery):
    text = (
        "<b>Добро пожаловать в ПРОСТОРЫ.НОВОСТРОЙКИ!</b>\n\n"
        "🚀 Современный инструмент продаж\n"
        "🎨 Персонализация под ваш бренд\n"
        "📊 Фильтры, карты, заявки в 1 клик\n"
        "📈 Увеличение конверсии до 50%\n"
        "💬 Простота и функциональность\n\n"
        "👇 <b>Вы агент и хотите продавать новостройки ПРОСТО и СОВРЕМЕННО?</b>\n"
        "Тогда регистрируйтесь и бесплатно тестируйте приложение 7 дней!\n\n"
        "✨ <b><i>ПРОСТОРЫ = Продавай + Красиво</i></b>"
    )
    await c.message.edit_text(text, reply_markup=welcome_kb(), parse_mode="HTML")
    await c.answer()

# === ЗАПУСК ===
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    logging.info("✅ Бот ПРОСТОРЫ запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()
    import asyncio
    asyncio.run(main())
