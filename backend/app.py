from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "🛡️ YakSafe LIVE!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run()
