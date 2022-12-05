import datetime

class Personajes:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def to_json(self):
        return{
            'Nombre':self.nombre
        }
