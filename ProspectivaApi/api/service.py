import json 

with open('api/ejemplo.json', 'r') as archivo:
    contenido_json = json.load(archivo)  


json_como_cadena = json.dumps(contenido_json)


print(json_como_cadena)