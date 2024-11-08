from pyexpat.errors import messages

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Now let's try to deploy to production environment with auto deploy application!!!")

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)