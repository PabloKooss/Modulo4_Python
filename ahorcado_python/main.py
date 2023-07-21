from menu import *
import pwinput
import sqlite3
print("**********************\n* Juego de ahorcado  *\n**********************")

while 0 <= (opcion= int(input('Elige una opción\nIngresar ---> 1\nRegustrar nuevo usuario ---> 2\nSalir ---> S'))) <= 3:
    Match opcion:
        case 1:
            verificar()
        case 2:
            registrar()
        case 3:
            print("Buen día")
            break
print("Opcion invalida")
