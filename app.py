from flask import Flask, jsonify, render_template
from flask.helpers import send_from_directory
from flask.wrappers import Response
from frase import FraseMod
import os

app = Flask('__name__')

respuesta = Response()
fraseMod = FraseMod()
respuesta.headers['Access-Control-Allow-Origin'] = '*'

#*#*#*#*#* /frases *#*#*#*#*#

@app.route('/frases', methods=['GET'])
def get_frases():
    global respuesta
    respuesta = jsonify(FraseMod.buscaFrases())
    return respuesta

@app.route('/frase', methods=['GET'])
def get_frase_random():
    global respuesta
    global fraseMod
    respuesta = jsonify(fraseMod.buscaFraseRandom())
    return respuesta

@app.route('/frase/<int:fraseId>', methods=['GET'])
def get_frase_id(fraseId):
    global respuesta
    respuesta = jsonify(FraseMod.buscaFraseId(fraseId))
    return respuesta

@app.route('/frase/personaje/<int:personajeId>', methods=['GET'])
def get_frase_personaje(personajeId):
    global respuesta
    respuesta = jsonify(FraseMod.buscaFrasePersonaje(personajeId))
    return respuesta

#*#*#*#*#* /personajes *#*#*#*#*#

@app.route('/personajes', methods=['GET'])
def get_persoanjes():
    global respuesta
    respuesta = jsonify(FraseMod.buscarPerosnajes())
    return respuesta

#*#*#*#*#* /capitulos *#*#*#*#*#

@app.route('/capitulos/temporada/<int:tempNro>', methods=['GET'])
def get_caps_temporada(tempNro):
    global respuesta
    respuesta = jsonify(FraseMod.capitulosPorTemporada(tempNro))
    return respuesta

@app.route('/capitulo/random', methods=['GET'])
def get_cap_random():
    global respuesta
    respuesta = jsonify(FraseMod.capituloRandom())
    return respuesta








if __name__ == '__main__':
    app.run(host='localhost', port = 3000, debug = True)

