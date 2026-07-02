# ПРОСТОРЫ.НОВОСТРОЙКИ Telegram Bot

A Telegram bot for the ПРОСТОРЫ.НОВОСТРОЙКИ real estate service. It greets agents, opens a Telegram Mini App catalog, and handles agent registration.

## Stack
- **Python** with `aiogram` 3.7.0 (async Telegram bot framework)
- **Flask** (`keep_alive.py`) — lightweight HTTP server on port 8080 to keep the process alive on Replit

## How to run
The workflow `Start application` runs `python bot.py`.

**Required secret:**
- `BOT_TOKEN` — Telegram bot token from @BotFather (stored as a Replit Secret)

## Project structure
- `bot.py` — main bot logic: commands, inline keyboards, callback handlers
- `keep_alive.py` — Flask server that listens on port 8080 to prevent Replit sleep
- `requirements.txt` — Python dependencies

## User preferences
- Bot token must always be read from the `BOT_TOKEN` environment secret, never hardcoded.
