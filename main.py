from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo, desde mi maquina"

if __name__ == "__main__":
    app.run()