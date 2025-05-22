from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/actions', methods=['GET'])
def get_actions():
    actions = [
        {"name": "show3DModel", "label": "نمایش مدل 3D"},
        {"name": "openSettings", "label": "باز کردن تنظیمات"},
    ]
    return jsonify(actions)

if __name__ == '__main__':
    app.run()
