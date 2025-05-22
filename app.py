from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Zohreh!'

@app.route('/oauth')
def oauth_redirect():
    code = request.args.get('code')
    return jsonify({"message": "Received code", "code": code})

@app.route('/api/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    return jsonify({"status": "received", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
