from .animal import Animal

class Anfibio(Animal):
    
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio.listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, Animal.getZona, "rojo", True)
        Anfibio.listado.append(rana)
        Anfibio.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, Animal.getZona, "negro y amarillo", False)
        Anfibio.listado.append(salamandra)
        Anfibio.salamandras += 1
        return salamandra

    @classmethod
    def getListado(cls):
        return Anfibio.listado
    
    @classmethod
    def setListado(cls, listado):
        Anfibio.listado = listado

    
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso