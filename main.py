 from flask import Flask, Response
import random
import string
import os

app = Flask(__name__)

def generate_random_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

@app.route('/generatekey')
def generate_key():
    return generate_random_key()

@app.route('/generatekey.html')
def key_page():
    key = generate_random_key()
    html = f"""
    <html>
    <head>
      <title>Generated Key</title>
    </head>
    <body style='background:#111;color:white;font-family:sans-serif;text-align:center;padding-top:50px;'>
      <h2>Your Generated Key</h2>
      <h1 id='key'>{key}</h1>
      <button onclick="navigator.clipboard.writeText('{key}');alert('Copied!')">📋 Copy</button>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
