from flask import Flask

app = Flask(__name__)

# funcudfkasjfkasfj
@app.route("/")
def hello_world():
    return {"nombre: joerlyn, apellido:morfe"}
