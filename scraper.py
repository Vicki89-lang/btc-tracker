import time
import random
def get_ohlc_data(symbol):
    data = []
    base = 60000 if symbol == "BTC" else 3000 if symbol == "ETH" else 150 if symbol== "SOL" else 80
    now = int(time.time() // 3600 * 3600) * 1000
    for i in range(24):
        t = now - ((23 - i) * 3600000)
        o = base + random.uniform(-50, 50)
        c = o + random.uniform(-40, 40)
        data.append({
            "x": t,
            "o": o,
            "h": max(o, c) + 10,
            "l": min(o, c) - 10,
            "c": c
        })
    return sorted(data, key=lambda d: d['x'])

