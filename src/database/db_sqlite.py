from decouple import config

import sqlite3

def getConnection():
    try:
        conn = sqlite3.connect(config('URL_DB'))
        # print('coneccion OK')
        return conn
    except Exception as ex: 
        print(ex)
    