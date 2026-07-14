from flask import Flask, render_template, jsonify
# Assuming your logic is in scraper.py
from scraper import get_ohlc_data 

app = Flask(__name__)

@app.route('/')
def index():
    # Serves your UI
    return render_template('index.html')

@app.route('/api/data/<symbol>')
def api_data(symbol):
    # API endpoint for your chart
    try:
        data = get_ohlc_data(symbol.upper())
        if not data:
            return jsonify({"error": "No data found"}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use 0.0.0.0 so it's accessible over local network
    app.run(host='0.0.0.0', port=5000, debug=True)

