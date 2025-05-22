import requests
#import urequests µ as requests 

respuesta= requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(respuesta.status_code)
datos=respuesta.json()
print(datos["title"])

sensado={
    "Temperatura":23,
    "Humedad":100,
    "Altura":3
}

respuesta= requests.post()
print(respuesta.status_code)