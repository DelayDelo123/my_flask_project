from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ya sosal'

if __name__ == '__main__':
    # Приложение будет слушать на всех сетевых интерфейсах на порту 5000
    app.run(host='0.0.0.0', port=5000)
