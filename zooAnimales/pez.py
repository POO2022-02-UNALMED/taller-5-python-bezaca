from .animal import Animal

class Pez(Animal):

    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero,Animal.getZona, "rojo", 6)
        Pez.listado.append(salmon)
        Pez.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, Animal.getZona, "gris", 6)
        Pez.listado.append(bacalao)
        Pez.bacalaos += 1
        return bacalao

    @classmethod
    def cantidadPeces(cls):
        return len(Pez.listado)

    @classmethod
    def getListado(cls):
        return Pez.listado
    
    @classmethod
    def setListado(cls, listado):
        Pez.listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas