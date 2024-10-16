
class Capitulo():

    def __init__(self, id, numero, nombre, temporada, descripcion, duracion, nroTotal) -> None:
        self.id = id
        self.numero = numero
        self.nombre = nombre
        self.temporada = temporada
        self.descripcion = descripcion
        self.duracion = duracion
        self.nroTotal = nroTotal

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'temporada' : self.temporada,
            'descripcion' : self.descripcion,
            'duracion' : self.duracion,
            'nroTotal' : self.nroTotal
        }