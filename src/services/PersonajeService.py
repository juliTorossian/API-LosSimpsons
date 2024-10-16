import traceback

from src.database.db_sqlite import getConnection
from src.utils.Logger import Logger, LoggerTypes
from src.models.PersonajeModel import Personaje

class PersonajeService():

    @classmethod
    def get_personajes(cls):
        try: 
            personajes = []
            conn = getConnection()
            cursor = conn.cursor()

            query = 'SELECT * FROM personaje'
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                personaje = Personaje(int(row[0]), row[1])
                personajes.append(personaje.to_json())
            conn.close()
            return personajes
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))
            Logger.add_to_log(LoggerTypes.ERROR, traceback.print_stack())

    @classmethod
    def get_personaje_id(cls, id):
        try: 
            personaje = None
            conn = getConnection()
            cursor = conn.cursor()

            query = 'SELECT * FROM personaje WHERE persId = {}'.format(id)
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                personaje = Personaje(int(row[0]), row[1]).to_json()
            conn.close()
            return personaje
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))
            Logger.add_to_log(LoggerTypes.ERROR, traceback.print_stack())