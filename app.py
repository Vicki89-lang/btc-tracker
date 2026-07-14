from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to serve the dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API route for chart data
@app.route('/api/data/<symbol>')
def get_data(symbol):
    # This is dummy data. Later, replace this with requests to CoinGecko API
    data = {
        "bitcoin": {"dates": ["Mon", "Tue", "Wed", "Thu", "Fri"], "prices": [60000, 62000, 61000, 63000, 65000]},
        "ethereum": {"dates": ["Mon", "Tue", "Wed", "Thu", "Fri"], "prices": [3000, 3100, 3050, 3200, 3300]}
    }
    return jsonify(data.get(symbol, {"dates": [], "prices": []}))

if __name__ == '__main__':
    app.run(debug=True)

