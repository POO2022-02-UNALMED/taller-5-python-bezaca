class Zoologico:
    def __init__(self, nombre, ubicacion, zonas = None ) -> None:
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def agregarZonas(self, zona):
        if self._zonas is None: self._zonas = []
        self._zonas.append(zona)


    def cantidadTotalAnimales(self):
        cantidad_animales = 0
        for z in self._zonas: cantidad_animales += len(z._animales)
        return cantidad_animales