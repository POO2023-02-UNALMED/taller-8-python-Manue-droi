from deportista import Deportista

class Futbolista(Deportista):
    _listaFutbolistas = []
    def __init__(self,nombre, edad, altura, sexo, anosPracticados, golesMarcados, tarjetasRojas, piernaHabil):
        super.__init__(nombre, edad, altura, sexo, "Futbol", anosPracticados)
        self._golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    #Meetodos get
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    
    