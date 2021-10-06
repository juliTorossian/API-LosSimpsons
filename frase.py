from sqlite3.dbapi2 import Cursor, connect
from conn import coneccion, closeConn
import random
import base64

class FraseMod():

    def buscaFrases():
        frases = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId'

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')

            frases.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64})
        
        return frases
    
    def buscaFraseRandom(self):
        frase = []
        conn = coneccion()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM frase')
        cant = len(cursor.fetchall())
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(random.randrange(cant))

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)
        for row in rows:
            # print(row)
            imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')

            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64})
        
        return frase

    def buscaFraseId(id):
        frase = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(id)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')

            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64})
        rows[0][1]
        return frase


    def buscaFrasePersonaje(id):
        frase = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE personaje.persId = {}'.format(id)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagen = '{}_550x550.jpg'.format(row[2].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')
            
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagen64})
        
        return frase

    def buscarPerosnajes():
        personajes = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT persNombre FROM personaje'

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagen = '{}_550x550.jpg'.format(row[0].replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')
            
            personajes.append({'nombre': row[0], 'imagen': imagen64})
        
        return personajes
    
    def capitulosPorTemporada(nroTemp):
        caps = []
        conn = coneccion()
        cursor = conn.cursor()

        query = 'SELECT * FROM capitulo WHERE capTemporada = {}'.format(nroTemp)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            caps.append({'capNumero': row[1], 'capNombre': row[2], 'capTemporada': row[3], 'capDesc': row[4], 'capTime': row[5], 'capNroTot': row[6]})
        
        return caps
    
    def capituloRandom():
        caps = []
        conn = coneccion()
        cursor = conn.cursor()

        cursor.execute('SELECT capNro FROM capitulo')
        cant = len(cursor.fetchall())
        
        query = 'SELECT * FROM capitulo WHERE capNroTot = {}'.format(random.randrange(cant))

        cursor.execute(query)
        rows = cursor.fetchall()

        closeConn(conn)
        for row in rows:
            # print(row)
            caps.append({'capNumero': row[1], 'capNombre': row[2], 'capTemporada': row[3], 'capDesc': row[4], 'capTime': row[5], 'capNroTot': row[6]})
        
        return caps


class Frase():
    fraseId   : int     
    frase     : str
    personaje : str

    def __init__(self, fraseId, frase, personaje):
        self.fraseId   = fraseId
        self.frase     = frase
        self.personaje = personaje


# frase = FraseMod()

# fr = frase.buscaFrases()

# for f in fr:
#     print(f.frase)