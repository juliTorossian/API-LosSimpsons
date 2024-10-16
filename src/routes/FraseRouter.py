from flask import Blueprint, request, jsonify

from src.services.FraseService import FraseService

main = Blueprint('frase_blueprint', __name__)

@main.route('/')
def get_frases():
    try:
        frases = FraseService.get_frases()
        if (len(frases) > 0):
            return jsonify({'frases': frases, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        print(ex)
        return jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})

@main.route('/random')
def get_frase_random():
    try:
        frase = FraseService.get_frase_random()
        if (len(frase) > 0):
            return jsonify({'frases': frase, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        print(ex)
        return jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
    
@main.route('/<int:id>')
def get_frase_id(id):
    try:
        frase = FraseService.get_frase_id(id)
        if (len(frase) > 0):
            return jsonify({'frases': frase, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        print(ex)
        return jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})