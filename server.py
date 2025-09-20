from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

signal = "NONE"

@app.route('/signal', methods=['GET'])
def get_signal():
    return jsonify({"signal": signal})

@app.route('/send/<action>', methods=['POST'])
def send_signal(action):
    global signal
    action_upper = action.upper()
    if action_upper in ["BUY", "SELL"]:
        signal = action_upper
        return jsonify({"signal": signal})
    return jsonify({"error": "Invalid action"}), 400

@app.route('/reset', methods=['POST'])
def reset_signal():
    global signal
    signal = "NONE"
    return jsonify({"signal": signal, "status":"reset"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
