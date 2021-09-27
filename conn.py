import sqlite3
from sqlite3.dbapi2 import Cursor, Error

def coneccion():
    try:
        conn = sqlite3.connect('losSimpsons.db')
        # print('coneccion OK')
        return conn
    except Error: 
        print('ah ocurrido un error en la coneccion a la BD')
    
def closeConn(conn):
    try:
        conn.close()
        # print('coneccion cerrada Ok')
    except Error:
        print('Error al cerrar la coneccion')
