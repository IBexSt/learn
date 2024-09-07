from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Чтобы разрешить запросы с фронтенда

# Пример простого API-эндпоинта
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)