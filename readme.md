# Binance Futures Testnet Trading Bot

## 📌 Overview

A Python-based CLI trading bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).
Built with a clean, modular architecture, proper input validation, and structured logging for reliability.

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/ked-1823/trading-bot.git
cd trading-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

> ⚠️ Ensure your Binance Futures Testnet account has sufficient USDT balance.

---

## 🚀 Usage

### ▶ Place MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### ▶ Place LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📄 Output

The CLI displays:

* Order request summary
* Success / failure message
* Order details:

  * `orderId`
  * `status`
  * `executedQty`
  * `avgPrice`

---

## 📊 Logging

All API interactions are logged in:

```
trading_bot.log
```

Includes:

* API request parameters
* API responses
* Error messages (if any)

---

## 🧱 Project Structure

```
trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py         # Binance API wrapper
│   ├── orders.py         # Order execution logic
│   ├── validators.py     # Input validation
│   ├── logging_config.py # Logging configuration
│
├── cli.py                # CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚠️ Assumptions

* Valid trading symbol is provided (e.g., BTCUSDT)
* Binance Futures Testnet account is active
* API keys are correct and have required permissions
* Sufficient test balance is available

---

## ✅ Features

* Market & Limit order support
* BUY and SELL operations
* CLI-based interface
* Input validation with clear error messages
* Structured logging (requests, responses, errors)
* Clean and modular code design

---

## 🧪 Example Logs

```
INFO | Order Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
INFO | Order Response: {'orderId': 123456, 'status': 'FILLED', ...}
```

---

## 🔒 Security Note

* Do NOT commit `.env` file to GitHub
* Regenerate API keys if they were accidentally exposed
* Use `.gitignore` to exclude sensitive files

---

## 📌 Submission Notes

This project meets the following requirements:

* Market & Limit orders on Binance Futures Testnet
* CLI-based input handling
* Structured logging
* Error handling and validation
* Modular and reusable code structure

---
