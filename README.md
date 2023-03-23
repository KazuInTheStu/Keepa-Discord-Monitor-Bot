# Discord-Keepa Price Tracker

This is a Python script that monitors the prices of products on Amazon using the Keepa API, and sends a Discord notification whenever the price of a product changes by a specified percentage threshold. ( Handy for those looking for pricing errors )

## Prerequisites

- Python 3.7 or higher
- Discord bot account
- Keepa API key

## Installation

1. Clone the repository:

git clone https://github.com/KazuInTheStu/Keepa-Discord-Monitor-Bot.git


2. Install the required packages:

pip install discord keepa asyncio


3. Replace the following placeholders in the script:

- `YOUR_DISCORD_BOT_TOKEN`: Replace with your Discord bot token.
- `YOUR_KEEPA_API_KEY`: Replace with your Keepa API key.
- `THRESHOLD`: Replace with your desired percentage change threshold.
- `CHANNEL_ID`: Replace with your desired Discord channel ID.

## Usage

1. Start the script by running the following command:

python price_tracker.py


2. The script will run continuously in the background and monitor the prices of products on Amazon. Whenever the price of a product changes by the specified percentage threshold, it will send a Discord notification with details about the product.

## Customization

- `marketplaces`: Replace with a list of Amazon site IDs you want to monitor (e.g. "com", "co.uk", "ca", etc.).
- `check_price()`: Modify the code inside this function to customize the notification message.

## Credits

- [Discord API](https://discordpy.readthedocs.io/en/stable/index.html)
- [Keepa API](https://keepa.com/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)

## License

This project is licensed under the [MIT License].
