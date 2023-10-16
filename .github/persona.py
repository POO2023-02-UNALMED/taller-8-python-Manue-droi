class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    
    #metodos get
    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getAltura(self):
        return self._altura
    def getSexo(self):
        return self._sexo
    
    #metodos set
    def setNombre(self, nombre):
        self._nombre = nombre
    def getEdad(self, edad):
        self._edad = edad
    def getAltura(self, altura):
        self._altura = altura
    def getSexo(self, sexo):
        self._sexo = sexo