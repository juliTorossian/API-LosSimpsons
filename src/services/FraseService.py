import base64
import random
import traceback

from src.database.db_sqlite import getConnection
from src.models.FraseModel import Frase
from src.utils.Logger import Logger


class FraseService():

    @classmethod
    def get_frases(cls):
        frases = []
        try:
            conn = getConnection()
            cursor = conn.cursor()
            
            query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId'
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()

            for row in rows:                
                frase = Frase(row[0], row[1], row[2])
                frases.append(frase.to_json())
            
            return frases
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.print_stack())

    @classmethod
    def get_frase_random(cls):
        frase = None
        try:
            conn = getConnection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM frase')
            cant = len(cursor.fetchall())
            
            query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(random.randrange(cant))
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            
            for row in rows:
                imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
                prefix = f'data:image/jpg;base64,'
                with open('src\\public\\img\\{}'.format(imagen), 'rb') as f:
                    img = f.read()
                imagen64 = prefix + base64.b64encode(img).decode('utf-8')

                frase = {'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64}
            
            return frase

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.print_stack())
            
    @classmethod
    def get_frase_id(cls, id):
        frase = None
        try:
            conn = getConnection()
            cursor = conn.cursor()
            
            
            query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(id)
            cursor.execute(query)
            row = cursor.fetchone()
            conn.close()

            print(row)

            
            # for row in rows:
            imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('src\\public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')

            frase = {'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64}
            
            print(frase)
            return frase

            
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.print_stack())