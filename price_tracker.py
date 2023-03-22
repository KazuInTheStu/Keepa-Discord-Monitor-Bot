import discord
import keepa
import asyncio

# Replace with your Discord bot token
TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# Replace with your Keepa API key
API_KEY = "YOUR_KEEPA_API_KEY"

# Replace with your desired percentage change threshold, i usually go for 60+ % for all pricing error related stuff
THRESHOLD = 10

# Replace with your desired Discord channel
CHANNEL_ID = 1234567890

client = discord.Client()

# Create a Keepa API client object
keepa_api = keepa.Keepa(API_KEY)

@client.event
async def on_ready():
    print(f"{client.user} Is now online")

async def check_price():
    # Replace with a list of Amazon site IDs you want to monitor (e.g. "com", "co.uk", "ca", etc.)
    marketplaces = ["com", "co.uk", "ca", "de", "fr", "it", "es", "com.mx", "com.br", "com.au", "nl", "in", "ae"]

    while True:
        # Get the list of all products from Keepa
        products = keepa_api.search(category=0, domainId=marketplaces)

        for product in products:
            # Get the ASIN of the product
            asin = product["asin"]

            # Get the price history of the product from Keepa
            price_history = keepa_api.query(asins=[asin], history=True, stats=True, deals=True, marketplace=marketplaces)

            # Get the current price and the price change percentage
            current_price = price_history[asin]["data"][-1][1]
            price_change = (current_price - price_history[asin]["data"][-2][1]) / price_history[asin]["data"][-2][1] * 100

            # Check if the price change percentage exceeds the threshold
            if abs(price_change) >= THRESHOLD:
                # Build the embed message
                embed = discord.Embed(title="Price Alert!", description=f"The price of ASIN {asin} has changed by {price_change:.2f}%.")

                # Add the price history chart image
                chart_url = price_history[asin]["stats"]["current"][0]
                embed.set_image(url=chart_url)

                # Add the current price and the price change percentage
                embed.add_field(name="Current Price", value=f"${current_price:.2f}")
                embed.add_field(name="Price Change Percentage", value=f"{price_change:.2f}%")

                # Mention everyone in the specified Discord channel or DM recipient
                channel = client.get_channel(CHANNEL_ID)
                await channel.send("@everyone", embed=embed)

        # Wait for the specified interval before checking the price again
        await asyncio.sleep(60)

# Start the price checking loop
client.loop.create_task(check_price())

# Run the Discord bot
client.run(TOKEN)
