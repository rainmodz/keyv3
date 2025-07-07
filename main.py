from flask import Flask, jsonify, Response
import random
import string

app = Flask(__name__)

# Generates a random key
def generate_random_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

# Serve raw key at /generatekey (used by script)
@app.route('/generatekey')
def generate_key():
    key = generate_random_key()
    return key

# Serve the HTML page at /generatekey.html
@app.route('/generatekey.html')
def key_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Generated Key</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1e1e1e;
          color: #fff;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          height: 100vh;
        }
        #keyBox {
          background-color: #333;
          padding: 20px;
          border-radius: 8px;
          margin-bottom: 15px;
          font-size: 18px;
          word-break: break-all;
        }
        button {
          padding: 10px 20px;
          background-color: #4CAF50;
          border: none;
          color: white;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
        }
        button:hover {
          background-color: #45a049;
        }
      </style>
    </head>
    <body>

      <h1>✅ Your Generated Key</h1>
      <div id="keyBox">Generating...</div>
      <button onclick="copyKey()">📋 Copy Key</button>

      <script>
        fetch('/generatekey')
          .then(res => res.text())
          .then(data => {
            document.getElementById('keyBox').textContent = data;
            setTimeout(() => {
              navigator.clipboard.writeText(data);
              document.querySelector("button").textContent = "✅ Key Copied!";
            }, 3000);
          });

        function copyKey() {
          const key = document.getElementById("keyBox").textContent;
          navigator.clipboard.writeText(key);
          document.querySelector("button").textContent = "✅ Key Copied!";
        }
      </script>

    </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')

# Set your port if needed (important for Render)
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # make sure it's 0.0.0.0 bound
    app.run(host='0.0.0.0', port=port)

