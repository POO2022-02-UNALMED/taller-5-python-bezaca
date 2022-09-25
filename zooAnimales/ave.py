from .animal import Animal

class Ave(Animal):

    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.listado.append(halcon)
        Ave.halcones +=1
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.listado.append(aguila)
        Ave.aguilas +=1 
        return aguila

    @classmethod
    def cantidadAves(cls):
        return len(Ave.listado)

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color