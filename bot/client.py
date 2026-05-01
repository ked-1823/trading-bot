import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )

        # IMPORTANT: switch to futures testnet
        self.client.FUTURES_URL = os.getenv("BASE_URL")

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)