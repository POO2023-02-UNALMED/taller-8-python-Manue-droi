from futbolista import Futbolista
from deportista import Deportista
from persona import Persona

if __name__ == "__main__":

   
    futbolista = Futbolista("Felipe Perez", 21, "1,56", "M", 8, 189, 7, "Izquierda")
    ok = False
    if (futbolista.__str__() == "Mi nombre es Felipe Perez soy profesional en el deporte Futbol Tengo 21 años de edad y llevo 8 años en el deporte"):
        ok = True
    
    print(futbolista.__str__())