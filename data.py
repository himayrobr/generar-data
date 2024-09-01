import random
from faker import Faker
import pymongo

fake = Faker()

# Definimos las salas y el número de filas por sala
salas = ["Sala 1", "Sala 2"]
filas_por_sala = 10

# Definimos los tipos de asientos y sus precios
tipos_asientos = {
    "normal": 10.00,
    "premium": 15.00
}

# Función para generar un asiento aleatorio
def generar_asiento(sala, fila, numero, tipo):
    return {
        "numero": numero,
        "fila": fila,
        "sala": sala,
        "estado": "disponible",
        "tipo": tipo,
        "precio": tipos_asientos[tipo]
    }

# Creamos una lista para almacenar los asientos
asientos = []

# Generamos los asientos
for sala in salas:
    for fila in range(filas_por_sala):
        for numero in range(1, 21):  # 20 asientos por fila
            if numero <= 5 or numero >= 16:  # Los primeros 5 y los últimos 5 son premium
                tipo = "premium"
            else:
                tipo = "normal"
            asiento = generar_asiento(sala, chr(ord('A') + fila), numero, tipo)
            asientos.append(asiento)

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cineCampus"]
collection = db["asiento"]

# Inserción de los asientos
collection.insert_many(asientos)