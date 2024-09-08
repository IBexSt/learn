from flask import Flask, jsonify

app = Flask(__name__)

# Простое API, которое возвращает данные
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from backend!"})

if __name__ == '__main__':
    app.run(debug=True)