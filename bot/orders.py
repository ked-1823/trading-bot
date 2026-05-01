import logging
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

def create_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # ✅ Step 1: Validate input
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        # ✅ Step 2: Prepare parameters
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": float(quantity)
        }

        if order_type.upper() == "LIMIT":
            params["price"] = float(price)
            params["timeInForce"] = "GTC"

        # ✅ Step 3: Log request
        logging.info(f"Order Request: {params}")

        # ✅ Step 4: Call API
        response = client.place_order(**params)

        # ✅ Step 5: Log response
        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Order Error: {str(e)}")
        raise