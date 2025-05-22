from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)  # فقط برای تست، در کنسول نمایش می‌دهد

    # اینجا می‌تونی داده‌ها رو پردازش یا ذخیره کنی

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()
