
import google.generativeai as genai
import json 
genai.configure(api_key="AIzaSyC9ZPx7CvNEa_CBo6_IUTaA1kd7JQ6vZjA") 
ejemplo = "ejemplo.json"
import json 


# Create the model
generation_config = {
  "temperature": 1.3,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 20000,
  "response_mime_type": "text/plain",
}


with open('api/ejemplo.json', 'r') as archivo:
    contenido_json = json.load(archivo)  
json_como_cadena = json.dumps(contenido_json)


with open('api/formato.json', 'r') as archivo1:
    contenidoformato_json = json.load(archivo1)  
formato_como_cadena = json.dumps(contenidoformato_json)

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("aplica todos los analisis adicionales , y reflejalos de manera numerica con el mismo usuario , retorna un archivo json"+ json_como_cadena)

print(response.text)