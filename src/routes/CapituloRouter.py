import traceback
from flask import Blueprint, request, jsonify

from src.utils.Logger import Logger, LoggerTypes
from src.services.CapituloService import CapituloService

main = Blueprint('capitulo_blueprint', __name__)

@main.route('/')
def get_capitulos():
    try: 
        capitulos = CapituloService.get_capitulos()
        if (len(capitulos) > 0):
            return jsonify({'capitulos': capitulos, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
    
@main.route('/random')
def get_capitulo_random():
    try: 
        capitulo = CapituloService.get_capitulo_random()
        if (len(capitulo) > 0):
            return jsonify({'capitulo': capitulo, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
    
@main.route('/temporada/<int:tempId>')
def get_capitulo_temporada(tempId):
    try: 
        capitulos = CapituloService.get_capitulo_temporada(tempId)
        if (len(capitulos) > 0):
            return jsonify({'capitulos': capitulos, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
    
@main.route('/<int:id>')
def get_capitulo_id(id):
    try: 
        capitulo = CapituloService.get_capitulo_id(id)
        if (len(capitulo) > 0):
            return jsonify({'capitulo': capitulo, 'message': "SUCCESS", 'success': True})
        else:
            return jsonify({'message': "NOT_FOUND", 'success': False})
    except Exception as ex:
        Logger.add_to_log(LoggerTypes.ERROR, str(ex))
        Logger.add_to_log(LoggerTypes.ERROR, traceback.format_exc())

        res = jsonify({'message': "INTERNAL_SERVER_ERROR", 'success': False})
        return res, 500
