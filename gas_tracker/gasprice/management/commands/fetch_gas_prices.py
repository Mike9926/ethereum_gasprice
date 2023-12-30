# fetch_gas_prices.py
from django.core.management.base import BaseCommand
from gasprice.models import GasPrice
from django.utils import timezone
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the Alchemy API key from the environment variables
alchemy_api_key = os.getenv("iH54-rX47Q5WCn6GhTn065dnd2842M7d")
alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/iH54-rX47Q5WCn6GhTn065dnd2842M7d"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

class Command(BaseCommand):
    help = "Fetches and stores gas prices from the Ethereum network"

    def handle(self, *args, **options):
        try:
            gas_price = w3.eth.gas_price
            transaction_speed = "fast"  # You can customize this based on your app's needs

            # Store gas price in the database
            GasPrice.objects.create(
                gas_price=gas_price,
                transaction_speed=transaction_speed,
                timestamp=timezone.now()
            )

            self.stdout.write(
                self.style.SUCCESS(f"Gas price updated: {gas_price} Wei (Transaction speed: {transaction_speed})")
            )
        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"Failed to fetch and store gas prices. Error: {e}")
            )
