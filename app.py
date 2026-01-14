from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Tutor IA funcionando"

@app.route("/api/tutor", methods=["POST"])
def tutor():
    data = request.get_json()
    pregunta = data.get("pregunta", "")

    respuesta = (
        "Buena pregunta. Observa el simulador "
        "y piensa qué ocurre antes de responder."
    )

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
