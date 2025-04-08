#flask
from flask import Flask, jsonify
import pandas as pd

app= Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje":"Hola esta es mi api"})

@app.route("/Menu")
def leer_menu():
    data=pd.read_excel("apiimensaje.xlsx")
    data=data.to_dict(orient="records")
    return jsonify(data)


    
 


if __name__=="__main__":
    app.run()