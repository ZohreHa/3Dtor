from flask import jsonify

def handler(request):
    return jsonify({"message": "OAuth redirect for Zohreh Plugin"})
