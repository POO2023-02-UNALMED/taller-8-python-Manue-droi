from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, anosPracticados):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._anosPracticados = anosPracticados

    #metodos get
    def getDeporte(self):
        return self._deporte
    def getAnosPracticados(self):
        return self._anosPracticados
    
    #metodos set
    def setDeporte(self, deporte):
        self._deporte = deporte
    def setAnosPracticados(self, anosPracticados):
       self._anosPracticados = anosPracticados
