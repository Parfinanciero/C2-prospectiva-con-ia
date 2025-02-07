from fastapi.responses import PlainTextResponse
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
load_dotenv()

modelkey = os.getenv("API_KEY")

def generate_response(data):
    genai.configure(api_key = modelkey) 

    generation_config = {
    "temperature": 1.3,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 20000,
    "response_mime_type": "text/plain",
    }


    json_como_cadena = json.dumps(data)

    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message("aplica todos los analisis adicionales , y reflejalos de manera numerica con el mismo usuario , retorna un archivo json"+ json_como_cadena +"recuerda solo mostrar los siguientes datos : gastos total 1800 categorias que debe tener nombre total porcentaje lo arganizas por fecha y muestras fecha total analisis_adicional  gasto_promedio_diario  variacion_gasto_diario  categoria_mayor_gasto debe tener nombre , total categoria_menor_gasto que debe tener nombre y total , la tendencia de gasto que debe ser decreceinte o creciente segun tu analisis y meta que debe tener , titulo ,monto de meta , monto actual progreso de porcentaje diferencia de monto proyeccion tiempo dias restantes estimados progreso en el tiempo ,la cadena que recibiras con los datos va a cambiar con el tiempo , pero por ahora no puedes cambiar el formato hasta que yo te lo diga explicitamente ")

    return PlainTextResponse(content=response.text) 