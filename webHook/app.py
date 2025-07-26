from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)  # fuerza la conversión a JSON, aunque no se declare como application/json
    print("Datos recibidos:")
    print(data)
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
