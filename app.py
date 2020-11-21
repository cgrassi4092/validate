from flask import Flask, CSRFProtect

csrf = CSRFProtect(app)
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run(debug=True)
