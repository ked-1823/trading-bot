import argparse
from bot.client import BinanceClient
from bot.orders import create_order
from bot.logging_config import setup_logger

# ✅ initialize logging
setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Required for LIMIT")

    args = parser.parse_args()

    client = BinanceClient()

    # ✅ Print clean summary
    print("\n--- Order Summary ---")
    print({
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
        "price": args.price
    })

    try:
        response = create_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ Order Placed Successfully")
        print({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        })

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()