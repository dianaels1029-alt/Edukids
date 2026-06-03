# ======================================================
# FILE 1: THE LIVE BACKEND & DATABASE (PythonAnywhere)
# WITH ADMOB CREDENTIALS INTEGRATION
# ======================================================
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "activated_players.json"

# AdMob Configuration - YOUR CREDENTIALS
ADMOB_PUBLISHER_ID = "pub-6872596196321341"
ADMOB_APP_ID = "ca-app-pub-6872596196321341~5290076037"
ADMOB_BANNER_ID = "ca-app-pub-6872596196321341/7456084694"
ADMOB_INTERSTITIAL_ID = "ca-app-pub-6872596196321341/9751075542"
ADMOB_REWARDED_ID = "ca-app-pub-6872596196321341/5266025304"

# Initialize local database file if it doesn't exist
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

# AdMob ads.txt configuration endpoint
@app.route('/ads.txt', methods=['GET'])
def ads_txt():
    """Serves ads.txt for AdMob compliance"""
    ads_txt_content = """google.com, pub-6872596196321341, DIRECT, f08c47fec0942fa0"""
    return ads_txt_content, 200, {'Content-Type': 'text/plain'}

@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    """Receives transaction data from PayPal when a parent pays R50."""
    data = request.json
    if data and data.get('event_type') == 'PAYMENT.CAPTURE.COMPLETED':
        # Extract the custom player name passed during checkout
        try:
            player_alias = data['resource']['custom_id'].upper().strip()
            
            # Load, update, and save the database
            with open(DB_FILE, "r") as f:
                database = json.load(f)
                
            database[player_alias] = "ACTIVE"
            
            with open(DB_FILE, "w") as f:
                json.dump(database, f)
                
            return jsonify({"status": "Player Activated"}), 200
        except KeyError:
            return jsonify({"status": "Missing Custom ID"}), 400
            
    return jsonify({"status": "Ignored"}), 200

@app.route('/check-license', methods=['GET'])
def check_license():
    """The mobile app calls this endpoint to verify access instantly."""
    player_alias = request.args.get('alias', '').upper().strip()
    
    with open(DB_FILE, "r") as f:
        database = json.load(f)
        
    if player_alias in database:
        return jsonify({"status": "UNLOCKED"}), 200
    return jsonify({"status": "LOCKED"}), 200

@app.route('/admob-config', methods=['GET'])
def admob_config():
    """Returns AdMob configuration for the mobile app"""
    return jsonify({
        "publisher_id": ADMOB_PUBLISHER_ID,
        "app_id": ADMOB_APP_ID,
        "banner_ad_unit": ADMOB_BANNER_ID,
        "interstitial_ad_unit": ADMOB_INTERSTITIAL_ID,
        "rewarded_ad_unit": ADMOB_REWARDED_ID
    }), 200

if __name__ == '__main__':
    app.run(debug=False)
