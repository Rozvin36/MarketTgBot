# Telegram Shop Bot

A Telegram bot for selling digital goods with payment system integration.

## Features

Product catalog with dynamic inline keyboard. Payments via Telegram Stars or other providers. Payment confirmation with price and product status validation. Redis caching. Purchase storage in PostgreSQL. Async architecture.

## Stack

Aiogram 3 — Telegram Bot API framework. SQLAlchemy 2.0 — ORM for database interactions. PostgreSQL — main database. Redis — caching.

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/telegram-shop-bot.git
cd telegram-shop-bot
```

### 2. Create a virtual environment

```
python -m venv .venv
```

```
source .venv/bin/activate
```
for Linux/Mac. Or
```
.venv\Scripts\activate
```
for Windows.

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Environment variables

Create a `.env` file in the project root with the following content:

```
BOT_TOKEN=your_bot_token
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=tgbot
REDIS_URL=redis://localhost:6379/0
```

- BOT_TOKEN — your bot token from BotFather
- POSTGRES_USER — PostgreSQL user
- POSTGRES_PASSWORD — PostgreSQL password
- POSTGRES_HOST — database host
- POSTGRES_PORT — database port
- POSTGRES_DB — database name
- REDIS_URL — Redis connection string

### 5. Start PostgreSQL and Redis

Make sure PostgreSQL and Redis are installed and running locally. Verify:

```
psql -U postgres -d tgbot
redis-cli ping
```

### 6. Create tables and seed test data

```
python core/seed.py
```

This script creates all tables and adds three test products.

### 7. Run the bot

```
python bot/main.py
```

## Project Structure

```
bot/main.py              — entry point, bot startup
bot/handlers/user.py     — user command handlers and product catalog
bot/handlers/payment.py  — payment processing handlers
bot/keyboards/inline.py  — inline keyboard generation
core/config.py           — environment variables loading
core/database.py         — database connection
core/models.py           — SQLAlchemy table models
core/redis.py            — Redis connection
core/seed.py             — test data seeding
core/enums.py            — enumerations
```

## How It Works

User starts the bot with /start. Bot responds with a welcome message. /buy command displays the product catalog with inline buttons. User selects a product. Bot creates a payment invoice via Telegram Stars or another payment provider. User confirms the payment. Bot validates the payment in pre_checkout_query: checks if the product exists, its status, and correct price. If everything is correct, bot confirms the payment. Telegram deducts the funds. Bot receives successful_payment, saves the purchase record in the database, and delivers the product.

## Payments

Default configuration uses Telegram Stars. To use another provider like YooKassa, modify the send_invoice parameters: set provider_token, change currency to RUB, and specify the amount in kopecks (cents).
