from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- YOUR PYDROID LOGIC LIVE ON THE BACKEND ---
# We set the gatekeeper variable to True when the server starts
victor_freeman = True

@app.route('/sing-song', methods=['GET'])
def play_song():
    global victor_freeman  # Tells Python to use the variable outside this function
    
    if victor_freeman == True:
        # The gate is open! Give the reward and flip the switch to False
        message = "Now singing: Heal The World 🎶 (Bonus Claimed!)"

        print("\n[BACKEND CALLED]: Reward successfully granted.")
    else:
        # The gate is closed because victor_freeman is now False
        message = "Access Denied: You have already claimed this song bonus!"
        print("\n[BACKEND CALLED]: Blocked a double-claim attempt.")
        
    return jsonify({"server_response": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


