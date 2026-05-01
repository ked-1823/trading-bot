# Binance Futures Testnet Trading Bot

## 📌 Overview
A simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## ⚙️ Setup Instructions

### 1. Clone repo
git clone <your-repo-link>
cd trading_bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Create .env file
Add your Binance Testnet API keys:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com

---

## 🚀 Usage

### ▶ Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### ▶ Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

## 📄 Output
The bot prints:
- Order summary
- Order status (success/failure)
- Key details (orderId, status, executedQty, avgPrice)

---

## 📊 Logging
All API requests, responses, and errors are logged in:
trading_bot.log

---

## 🧱 Project Structure
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md

---

## ⚠️ Assumptions
- User provides valid symbol (e.g., BTCUSDT)
- Testnet account has sufficient balance
- Internet connection is stable

---

## ✅ Features
- Market & Limit order support
- CLI-based input
- Input validation
- Logging & error handling
- Clean modular structure