from deportista import Deportista

class Futbolista(Deportista):
    _listaFutbolistas = []


    def __init__(self,nombre, edad, altura, sexo, anosPracticados, golesMarcados, tarjetasRojas, piernaHabil):
        super.__init__(nombre, edad, altura, sexo, "Futbol", anosPracticados)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    #Meetodos get
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    
    #Meetodos set
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil


    @classmethod
    def setListaFutbolistas(cls, futbolistas):
        cls._listaFutbolistas = futbolistas
     
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas



    def __str__(self) :
       cadena = "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAnosPracticados()))
       return cadena
    
    if __name__ == "__main__":
     futbolista = ("Felipe Perez", 21, "1,56", "M", 8, 189, 7, "Izquierda")
     print(futbolista.__str__())
    