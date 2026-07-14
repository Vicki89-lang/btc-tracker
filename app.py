import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Map your ticker symbols to CoinGecko IDs
COIN_MAP = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "solana": "solana",
    "doge": "dogecoin"
}

@app.route('/api/data/<symbol>')
def get_data(symbol):
    coin_id = COIN_MAP.get(symbol.lower())
    if not coin_id:
        return jsonify({"error": "Coin not found"}), 404

    # Fetch live price from CoinGecko
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url).json()
    
    # Return current price to the chart
    price = response.get(coin_id, {}).get('usd', 0)
    return jsonify({"dates": ["Now"], "prices": [price]})

