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
      <style>
        body {{
          background-color: #121212;
          color: white;
          font-family: Arial;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          height: 100vh;
        }}
        .box {{
          background: #1e1e1e;
          padding: 20px;
          border-radius: 8px;
          margin: 10px;
        }}
      </style>
    </head>
    <body>
      <div class="box">
        <h2>Your Key:</h2>
        <code id="key">{key}</code><br><br>
        <button onclick="copyKey()">📋 Copy</button>
      </div>
      <script>
        function copyKey() {{
          const text = document.getElementById("key").textContent;
          navigator.clipboard.writeText(text);
          alert("Key copied: " + text);
        }}
      </script>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
