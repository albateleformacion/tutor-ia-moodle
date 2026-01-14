from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# ⚠️ Tu clave debe estar como variable de entorno
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
        respuesta = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        texto_respuesta = respuesta.choices[0].text.strip()
    except Exception as e:
        texto_respuesta = f"Error: {str(e)}"

    return jsonify({"respuesta": texto_respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
