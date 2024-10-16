import base64
from src.utils.Logger import Logger, LoggerTypes

class Personaje():

    def __init__(self, id, nombre) -> None:
        self.id = id
        self.nombre = nombre

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'imagen': self.get_imagen_base64()
        }
    
    def get_imagen_base64(self):
        try:
            imagen = '{}_550x550.jpg'.format(self.nombre.replace(' ',''))
            prefix = f'data:image/jpg;base64,'
            with open('src\\public\\img\\{}'.format(imagen), 'rb') as f:
                img = f.read()
            imagen64 = prefix + base64.b64encode(img).decode('utf-8')
            return imagen64
        except OSError as esex:
            Logger.add_to_log(LoggerTypes.WARNING, str(esex))
        except Exception as ex:
            Logger.add_to_log(LoggerTypes.ERROR, str(ex))

