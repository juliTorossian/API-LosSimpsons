import traceback
from flask import Blueprint, request, jsonify

from src.utils.Logger import Logger, LoggerTypes
from src.services.PersonajeService import PersonajeService

main = Blueprint('personaje_blueprint', __name__)

@main.route('/')
def get_personajes():
    try: 
        personajes = PersonajeService.get_personajes()
        if (len(personajes) > 0):
            return jsonify({'personajes': personajes, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
    
@main.route('/<int:id>')
def get_personaje_id(id):
    try: 
        personaje = PersonajeService.get_personaje_id(id)
        if (len(personaje) > 0):
            return jsonify({'personaje': personaje, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
