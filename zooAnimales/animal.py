"""""
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
"""

class Animal:
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona) -> None:
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.totalAnimales+=1
    
    """"
    @staticmethod
    def totalPorTipo():
        return f'''
        Mamiferos: {Mamifero.cantidadMamiferos()}\n
        Aves: {Ave.cantidadAves()}\n
        Reptiles: {Reptil.cantidadReptiles()}\n
        Peces: {Pez.cantidadPeces()}\n
        Anfibios: {Anfibio.cantidadAnfibios()}'''
    """

    def __str__(self) -> str:
        if self._zona is None:
            return f'''Mi nombre es {self._nombre}, tengo una edad de {self._edad},
            habito en {self._habitat} y mi genero es {self._genero}'''
        else:
            return f'''Mi nombre es {self._nombre}, tengo una edad de {self._edad},
            habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona},
            en el {self._zona._zoo}'''

    
    @classmethod
    def getTotalAnimales(cls):
        return Animal.getTotalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        Animal.totalAnimales = totalAnimales

    def getNombre(self):
        return self._nombre 

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona
    
    
  