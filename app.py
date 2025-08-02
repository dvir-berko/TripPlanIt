from flask import Flask, request, jsonify

app = Flask(__name__)

trips = []

@app.route('/trips', methods=['GET', 'POST'])
def handle_trips():
    if request.method == 'POST':
        data = request.get_json()
        trips.append(data)
        return jsonify({"message": "Trip added!", "trip": data}), 201
    return jsonify(trips)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
