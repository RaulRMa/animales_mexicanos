import sqlite3
import time
from sqlite3 import Error

animal = 1
db = 'animales.db'

def crea_conexion(db):
    """Crea una conexión con la base de datos SQLite"""
    con = None
    try:
        con = sqlite3.connect(db)
        print("Conexion creada con exito: %s"%(db))
        return con
    except Error as e:
        print(e)
    return con


def crea_tabla(conexion):
    crea_tabla = """CREATE TABLE Animales (
        id integer PRIMARY KEY AUTOINCREMENT,
        nombre varchar,
        descripcion text,
        nombre_cientifico varchar,
        tipo varchar,
        imagen blob
        ); """
    try:
        c = conexion.cursor()
        c.execute(crea_tabla)
    except Error as e:
        print(e)

def obten_informacion(animal,db):
    con = crea_conexion(db)
    query = """SELECT * from animales WHERE id = ?"""
    cur = con.cursor()
    result = cur.execute(query,(animal,))
    result = result.fetchone()
    
    ejemplar = {
        "nombre": result[1],
        "descripcion": ("No registrado", result[2])[result[2] != None],
        "nombreCientifico": ("No registrado", result[3])[result[3] != None],
        "tipo": ("No registrado", result[4])[result[4] != None],
        "imagen": (None, result[5])[result[5] != None]
    }
    return ejemplar

def inserta_animal(animal, db):
    con = crea_conexion(db)
    query = ''' INSERT INTO animales (nombre,descripcion,tipo,imagen)
	VALUES (?,?,?,?) '''
    img = convertToBinaryData(animal["imagen"])
    try:
        cur = con.cursor()
        tupla = (animal["nombre"], animal["descripcion"], animal["tipo"], img)
        cur.execute(query, tupla)
        con.commit()
        print("Se ha agregado con éxito")
        print(cur.lastrowid)
        return cur.lastrowid
    except Error as e:
        print("Ocurrió un error al intentar insertar en la base de datos")
        print(e)

def obten_imagenes(db):
    con = crea_conexion(db)
    query = ''' SELECT imagen from animales WHERE imagen IS NOT NULL '''
    try:
        cur = con.cursor()
        result = cur.execute(query).fetchall()
        return result
    except Error as e:
        print("Ocurrió un error al obtener las imágenes")
        print(e)


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

obten_informacion(animal,db)