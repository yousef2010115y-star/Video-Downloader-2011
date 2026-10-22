from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "app": "Video Downloader",
        "status": "online",
        "message": "Server is running"
    })

@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.post("/api/video/info")
def video_info():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").strip()

    if not url.startswith(("https://", "http://")):
        return jsonify({
            "error": "Please provide a valid HTTP or HTTPS URL"
        }), 400

    return jsonify({
        "status": "received",
        "message": "URL received. Download support is not configured yet."
    }), 200

if __name__ == "__main__":
    app.run()
