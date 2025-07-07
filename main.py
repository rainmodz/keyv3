from flask import Flask, jsonify
import random
import string
import os

app = Flask(__name__)

# Example simple key DB (replace with JSON file or DB later)
valid_keys = []

def generate_key(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def home():
    return "✅ Key System Running"

@app.route('/generatekey')
def gen_key():
    key = generate_key()
    valid_keys.append(key)
    return key  # returns key as plain text

@app.route('/verifykey')
def verify_key():
    from flask import request
    key = request.args.get("key")
    hwid = request.args.get("hwid")

    if key in valid_keys:
        return jsonify({"success": True, "hwid": hwid})
    return jsonify({"success": False, "message": "Invalid key"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

