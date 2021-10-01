from flask import Flask, jsonify, render_template
from flask.helpers import send_from_directory
from frase import FraseMod
import os

app = Flask('__name__')

@app.route('/frases', methods=['GET'])
def get_frases():
    return jsonify(FraseMod.buscaFrases())

@app.route('/frase', methods=['GET'])
def get_frase_random():
    respuesta = jsonify(FraseMod.buscaFraseRandom())
    respuesta.headers['Access-Control-Allow-Origin'] = '*'
    return respuesta

@app.route('/frase/<int:fraseId>', methods=['GET'])
def get_frase_id(fraseId):
    return jsonify(FraseMod.buscaFraseId(fraseId))

@app.route('/frase/personaje/<int:personajeId>', methods=['GET'])
def get_frase_personaje(personajeId):
    return jsonify(FraseMod.buscaFrasePersonaje(personajeId))

@app.route('/personajes', methods=['GET'])
def get_persoanjes():
    return jsonify(FraseMod.buscarPerosnajes())

@app.route('/imagen/<string:nombreIMG>')
def get_image(nombreIMG):
    # return '<img src="./public/img/{}_550x550.jpg" alt="imagen">'.format(nombreIMG)
    return send_from_directory(os.getcwd() +'/public/img/{}_550x550.jpg'.format(nombreIMG),path='./public/img/{}_550x550.jpg'.format(nombreIMG) , filename=nombreIMG)


@app.route('/capitulos/temporada/<int:tempNro>', methods=['GET'])
def get_caps_temporada(tempNro):
    return jsonify(FraseMod.capitulosPorTemporada(tempNro))

@app.route('/capitulo/random', methods=['GET'])
def get_cap_random():
    return jsonify(FraseMod.capituloRandom())

if __name__ == '__main__':
    app.run(host='192.168.0.172', port = 3000, debug = True)

