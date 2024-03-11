from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated data in the "database"
database_data = []

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json.get('data', None)

    if data:
        # Simulate updating the "database"
        database_data.append(data)
        print(f"Received data from ESP32: {data}")

        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'No data received'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
