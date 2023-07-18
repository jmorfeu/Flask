from flask import Flask

app = Flask(__name__)
#3e3432
@app.route("/")
def hello_world():
    return {"nombre: joerlyn, apellido:morfe"}
