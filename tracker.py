import requests
import time

def fetch_btc():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # Using a tuple for (connect_timeout, read_timeout)
            response = requests.get(url, timeout=(5, 15))
            response.raise_for_status()
            data = response.json()
            return data['bitcoin']['usd']
        
        except requests.exceptions.ReadTimeout:
            print(f"Read timeout on attempt {attempt + 1}. Retrying...")
            time.sleep(2)  # Wait 2 seconds before retrying
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break
    return None

# Your main loop
while True:
    price = fetch_btc()
    if price:
        print(f"Logged: {time.strftime('%Y-%m-%d %H:%M:%S')} | ${price}")
    time.sleep(60)

