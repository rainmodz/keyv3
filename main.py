from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
KEY_FILE = "keys.json"

# Load or create key store
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "w") as f:
        json.dump({}, f)

def load_keys():
    with open(KEY_FILE, "r") as f:
        return json.load(f)

def save_keys(data):
    with open(KEY_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return "✅ Key System Running"

@app.route("/verifykey")
def verify_key():
    key = request.args.get("key")
    hwid = request.args.get("hwid")

    if not key or not hwid:
        return jsonify({ "success": False, "message": "Missing key or hwid." }), 400

    data = load_keys()

    if key in data:
        if data[key] == hwid:
            return jsonify({ "success": True })
        else:
            return jsonify({ "success": False, "message": "Key used on another device." })
    else:
        # Save new HWID if unused
        data[key] = hwid
        save_keys(data)
        return jsonify({ "success": True })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
