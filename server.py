from flask import Flask, request, jsonify

app = Flask(__name__)

signal_status = "NONE"

@app.route("/signal", methods=["GET"])
def get_signal():
    return jsonify({"signal": signal_status})

@app.route("/signal", methods=["POST"])
def set_signal():
    global signal_status
    data = request.get_json()
    if not data or "signal" not in data:
        return jsonify({"error": "Invalid request"}), 400

    if data["signal"].upper() in ["BUY", "SELL"]:
        signal_status = data["signal"].upper()
        return jsonify({"status": "ok", "signal": signal_status})
    return jsonify({"error": "Signal must be BUY or SELL"}), 400

@app.route("/reset", methods=["POST"])
def reset_signal():
    global signal_status
    signal_status = "NONE"
    return jsonify({"status": "reset", "signal": signal_status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
