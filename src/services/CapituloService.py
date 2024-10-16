import traceback
import random

from src.database.db_sqlite import getConnection
from src.utils.Logger import Logger, LoggerTypes
from src.models.CapituloModel import Capitulo

class CapituloService():

    @classmethod
    def get_capitulos(cls):
        try: 
            capitulos = []
            conn = getConnection()
            cursor = conn.cursor()

            query = 'SELECT * FROM capitulo'
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                capitulo = Capitulo(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])
                capitulos.append(capitulo.to_json())
            conn.close()
            return capitulos
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))
            Logger.add_to_log(LoggerTypes.ERROR, traceback.print_stack())

    @classmethod
    def get_capitulo_id(cls, id):
        try: 
            capitulo = None
            conn = getConnection()
            cursor = conn.cursor()

            query = 'SELECT * FROM capitulo WHERE capId = {}'.format(id)
            cursor.execute(query)
            row = cursor.fetchone()
            conn.close()

            capitulo = Capitulo(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]).to_json()
            return capitulo
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))
            Logger.add_to_log(LoggerTypes.ERROR, traceback.print_stack())
            
    @classmethod
    def get_capitulo_random(cls):
        capitulo = None
        try:
            conn = getConnection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM capitulo')
            cant = len(cursor.fetchall())
            
            query = 'SELECT * FROM capitulo WHERE capId = {}'.format(random.randrange(cant))
            cursor.execute(query)
            row = cursor.fetchone()
            conn.close()

            capitulo = Capitulo(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]).to_json()
            return capitulo

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.print_stack())
        
    @classmethod
    def get_capitulo_temporada(cls, temporada):
        try: 
            capitulos = []
            conn = getConnection()
            cursor = conn.cursor()

            query = 'SELECT * FROM capitulo WHERE capTemporada = {}'.format(temporada)
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()

            for row in rows:
                capitulo = Capitulo(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])
                capitulos.append(capitulo.to_json())
            return capitulos
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))
            Logger.add_to_log(LoggerTypes.ERROR, traceback.print_stack())