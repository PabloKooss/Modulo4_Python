import sqlite3
from usuario.login import *
from usuario.registro import *


# Crear una conexión a la base de datos (o conectar a una existente)
conn = sqlite3.connect('usuarios.db')

# Crear un cursor para ejecutar las consultas
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
''')

# Hacer commit para guardar los cambios
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()


print("**********************\n* Juego de ahorcado  *\n**********************")
opcion= int(input('Elige una opción\nIngresar ---> 1\nRegustrar nuevo usuario ---> 2\nSalir ---> S\n'))
while 0 <= opcion <= 3:
    match opcion:
        case 1:
            verificar()
            break
        case 2:
            Registro()
            break
        case 3:
            print("Buen día")
            break
print("Fin de juego")
