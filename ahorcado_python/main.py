from menu import *
import pwinput
print("**********************\n* Juego de ahorcado  *\n**********************")
usu=pwinput.pwinput(prompt='Usuario: ')
contra=pwinput.pwinput(prompt='Contraseña: ')

if usu=="usuario" and contra=="1234":
    menu()   
else:
    print("\n\n------Datos incorrectos-----\n¡¡¡¡Buen dia!!!")