from niveles.nivel1 import jugar_N1
from niveles.nivel2 import juego_n2
from niveles.nivel3 import juego_n3
from niveles.nivel4 import juego_n4

def menu():
    print("Seleciona una opcion")
    print(" Opcion          1\n Opcion          2\n Opcion          3\n Opcion          4\n")
    opcion=int(input())
        
    match opcion:
        case 1:
            jugar_N1()
            
        case 2:
            juego_n2()
            
        case 3:
            juego_n3()
            
        case 4:
            juego_n4()
            
        case _:
            print("Elige una opcion valida")
            
    print("Buen dia")