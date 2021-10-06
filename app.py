from flask import Flask, jsonify, render_template
from flask.helpers import send_from_directory
from flask.wrappers import Response
from frase import FraseMod
import os

app = Flask('__name__')


#*#*#*#*#* /frases *#*#*#*#*#

@app.route('/frases', methods=['GET'])
def get_frases():
    respuesta = jsonify(FraseMod.buscaFrases())
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

@app.route('/frase', methods=['GET'])
def get_frase_random():
    respuesta = jsonify(FraseMod.buscaFraseRandom())
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

@app.route('/frase/<int:fraseId>', methods=['GET'])
def get_frase_id(fraseId):
    respuesta = jsonify(FraseMod.buscaFraseId(fraseId))
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

@app.route('/frase/personaje/<int:personajeId>', methods=['GET'])
def get_frase_personaje(personajeId):
    respuesta = jsonify(FraseMod.buscaFrasePersonaje(personajeId))
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

#*#*#*#*#* /personajes *#*#*#*#*#

@app.route('/personajes', methods=['GET'])
def get_persoanjes():
    respuesta = jsonify(FraseMod.buscarPerosnajes())
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

#*#*#*#*#* /capitulos *#*#*#*#*#

@app.route('/capitulos/temporada/<int:tempNro>', methods=['GET'])
def get_caps_temporada(tempNro):
    respuesta = jsonify(FraseMod.capitulosPorTemporada(tempNro))
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

@app.route('/capitulo/random', methods=['GET'])
def get_cap_random():
    respuesta = jsonify(FraseMod.capituloRandom())
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta








if __name__ == '__main__':
    app.run(host='localhost', port = 3000, debug = True)

