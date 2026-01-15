from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Tutor IA funcionando con ChatGPT"

@app.route("/api/tutor", methods=["POST"])
def tutor():
    data = request.get_json()
    pregunta = data.get("pregunta", "")

    # Prompt pedagógico Nivel 2
    prompt = f"""
Eres un tutor de física de secundaria que ayuda a los alumnos a entender la ley de Hooke.
Nunca des la respuesta directa. Solo guía con preguntas, ejemplos o pistas.
Pregunta del alumno: {pregunta}
Respuesta pedagógica:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un tutor pedagógico experto de física."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        texto_respuesta = response.choices[0].message.content.strip()
    except Exception as e:
        texto_respuesta = f"Error: {str(e)}"

    return jsonify({"respuesta": texto_respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
