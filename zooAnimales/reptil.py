from .animal import Animal

class Reptil(Animal):
     
    listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, largoCola) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, Animal.getZona,"verde", 3)
        Reptil.listado.append(iguana)
        Reptil.iguanas +=1 
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, Animal.getZona ,"blanco", 1)
        Reptil.listado.append(serpiente)
        Reptil.serpientes += 1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil.listado)

    @classmethod
    def getListado(cls):
        return Reptil.listado
    
    @classmethod
    def setListado(cls, listado):
        Reptil.listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    
