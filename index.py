from flask import Response

def handler(request):
    return Response("Hello from Zohreh Plugin!", mimetype="text/plain")
