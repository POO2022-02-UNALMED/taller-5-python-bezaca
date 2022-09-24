class Zona:
    def __init__(self, nombre, zoo = None, animales = None) -> None:
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    def agregarAnimales(self, animal):
        if self._animales is None: self._animales = []
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)