from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/api/webhook', methods=['POST'])
def webhook():
    auth = request.headers.get('Authorization')
    if auth != 'Bearer MySecretToken123456':
        abort(401)  # دسترسی غیرمجاز

    data = request.json
    print("Received webhook data:", data)

    # پردازش داده‌ها

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()
