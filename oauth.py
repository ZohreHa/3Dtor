from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

@app.route('/oauth')
def oauth_redirect():
    code = request.args.get('code')
    if not code:
        return jsonify({"error": "Missing code parameter"}), 400

    # اینجا باید کد رو برای گرفتن توکن استفاده کنی
    # مثلا درخواست به دیوار بزنی و توکن رو دریافت کنی
    # فعلا فقط پیام موفقیت رو می‌فرستیم

    return jsonify({"message": "Received OAuth code", "code": code})

if __name__ == '__main__':
    app.run()
