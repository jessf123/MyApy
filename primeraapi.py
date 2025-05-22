#flask
from flask import Flask, jsonify, request
import psycopg2
import json
URL="postgresql://jesse:NuIyzDWW4PVYHCF7HVRjPrKdMdzGbdi0@dpg-d0d4vq15pdvs73f7o7ag-a.oregon-postgres.render.com/pokemones_nqom"

conn = psycopg2.connect(URL)
cursor=conn.cursor()

app= Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({"mensaje":"Hola soy un pokedex, tengo varias funciones"})

#("1", "Bulbasaur", "Planta", "Veneno","https://www.google.com/imgres?q=bulbasaur&imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fpokemon%2Fimages%2F1%2F19%2FAsh_Bulbasaur.png%2Frevision%2Flatest%3Fcb%3D20230211060446&imgrefurl=https%3A%2F%2Fpokemon.fandom.com%2Fwiki%2FAsh%2527s_Bulbasaur&docid=DHnbOwLQfSWptM&tbnid=BKQPcwykTqVI1M&vet=12ahUKEwisrre6w5SNAxVQI0QIHSCFHVcQM3oECG8QAA..i&w=1920&h=1080&hcb=2&ved=2ahUKEwisrre6w5SNAxVQI0QIHSCFHVcQM3oECG8QAA")
@app.route("/nuevo/<Numero>/<Nombre>/<Tipo1>/<Tipo2>")
def agregar_pokemon(Numero,Nombre,Tipo1,Tipo2):
    conn = psycopg2.connect(URL)
    cursor=conn.cursor()
    try: 
        
        cursor.execute(
        "ISERT INTO kanto (numero,nombre,tipo1,tipo2) VALUES (%s,%s,%s,%s)",(Numero,Nombre,Tipo1,Tipo2))
        conn.commit()
        mensaje= f"{Nombre} agregado con exito"

    except psycopg2.errors.UniqueViolation as e:
        mensaje= f"El numero {Numero} o {Nombre} ya estaban registrados"
        conn.rollback()
    
    cursor.close()
    conn.close()
    return mensaje


@app.route("/subir_pokemon",methods={"POST"})
def agregar_pokemon_de_archivo():
    archivo= request.files["archivo"]
    if archivo and archivo.filename.endswith(".json"):
        contenido=json.load(archivo)
        conn = psycopg2.connect(URL)
        cursor=conn.cursor()
    try: 
        Nombre = contenido.get("Nombre")
        Numero = contenido.get("Numero")
        Tipo1 = contenido.get("Tipo1")
        Tipo2 = contenido.get("Tipo2")
        Imagen = contenido.get("Imagen")

        cursor.execute(
        "ISERT INTO kanto (numero,nombre,tipo1,tipo2,imagen) VALUES (%s,%s,%s,%s,%s)",(Numero,Nombre,Tipo1,Tipo2,Imagen))
        conn.commit()
        mensaje= f"{Nombre} agregado con exito"

    except psycopg2.errors.UniqueViolation as e:
        mensaje= f"El numero {Numero} o {Nombre} ya estaban registrados"
        conn.rollback()
    
    cursor.close()
    conn.close()
    return mensaje

    

@app.route("/verpokemons")
def ver_pokemons():
    conn = psycopg2.connect(URL)
    cursor=conn.cursor()
    cursor.execute(
    "SELECT *FROM kanto;")
    filas=cursor.fetchall()
    cursor.close()
    conn.close()

    return filas

@app.route("/verTipo/<tipo>")
def ver_pokemons_tipo(tipo):
    conn = psycopg2.connect(URL)
    cursor=conn.cursor()
    cursor.execute(
    "SELECT * FROM kanto WHERE Tipo1 = %s OR Tipo2 = %s ;", (tipo,tipo))
    filas=cursor.fetchall()
    cursor.close()
    conn.close()

    return filas

if __name__=="__main__":
    app.run()