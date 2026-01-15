from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Cliente OpenAI (NUEVA API)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Tutor IA funcionando con OpenAI (API nueva)"

@app.route("/api/tutor", methods=["POST"])
def tutor():
    data = request.get_json()
    pregunta = data.get("pregunta", "")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un tutor de física de secundaria. "
                        "Ayudas al alumno a comprender la ley de Hooke. "
                        "Nunca des la respuesta directa: guía con preguntas, pistas y ejemplos."
                    )
                },
                {
                    "role": "user",
                    "content": pregunta
                }
            ],
            temperature=0.7,
            max_tokens=150
        )

        texto_respuesta = response.choices[0].message.content.strip()

    except Exception as e:
        print("ERROR OPENAI:", e)
        texto_respuesta = f"Error interno IA: {str(e)}"

    return jsonify({"respuesta": texto_respuesta})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
