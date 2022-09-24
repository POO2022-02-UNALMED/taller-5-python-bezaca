from .animal import Animal

class Mamifero(Animal):

    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, zona, patas) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, Animal.getZona ,True, 4)
        Mamifero.listado.append(caballo)
        Mamifero.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, Animal.getZona, True, 4)
        Mamifero.listado.append(leon)
        Mamifero.leones += 1
        return leon

    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero.listado)