from sqlite3.dbapi2 import Cursor, connect
from conn import coneccion, closeConn
import random

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
            frases.append({'id': row[0], 'frase': row[1], 'personaje': row[2]})
        
        return frases
    
    def buscaFraseRandom():
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
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
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
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
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
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
        return frase

    def buscarPerosnajes():
        personajes = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT persNombre FROM personaje WHERE persId = {}'.format(id)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ',''))
            personajes.append({'id': row[0], 'nombre': row[1], 'imagen': imagenURL})
        
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