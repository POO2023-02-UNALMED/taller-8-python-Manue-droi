from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, AñosPracticando):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._AñosPracticando = AñosPracticando

    #metodos get
    def getDeporte(self):
        return self._deporte
    def getAñosPracticando(self):
        return self._AñosPracticando
    
    #metodos set
    def setDeporte(self, deporte):
        self._deporte = deporte
    def setAnosPracticados(self, AñosPracticando):
       self._AñosPracticando = AñosPracticando