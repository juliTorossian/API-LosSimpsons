
class Frase():

    def __init__(self, id, frase, personaje) -> None:
        self.id = id
        self.frase = frase
        self.personaje = personaje

    def to_json(self):
        return {
            'id': self.id,
            'frase': self.frase,
            'personaje': self.personaje
        }