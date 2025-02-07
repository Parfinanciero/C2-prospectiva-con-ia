from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from service import generate_response
from typing import Dict

from py_eureka_client.eureka_client import EurekaClient


# Configurar el cliente de Eureka
eureka_client = EurekaClient(
    eureka_server="http://localhost:8761/eureka",  # URL del servidor de Eureka
    app_name="python-microservice",               # Nombre del servicio en Eureka
    instance_port=5000,                           # Puerto del servicio
    instance_host="localhost"                     # IP o hostname del servicio
)

# Registrar el servicio en Eureka
eureka_client.start()


app = FastAPI()
@app.post("/prospectiva")
async def root(data: Dict) -> PlainTextResponse:
    
    return generate_response(data)

