from fastapi import FastAPI, HTTPException
from .db import get_database_connection
import pyodbc
from typing import List, Optional
from .schemas import Cliente
from datetime import datetime
from datetime import date

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de la cooperativa financiera"}

@app.get("/clientes")
async def obtener_clientes():
    try:
        conexion = get_database_connection()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()

        # Convertir las filas de la tabla en una lista de diccionarios
        lista_clientes = []
        for cliente in clientes:
            cliente_dict = {
                "id": cliente[0],
                "nombre": cliente[1],
                "apellido": cliente[2],
                "fecha de nacimiento": cliente[3],
                "correo": cliente[5],
                "direccion": cliente[6],
                "telefono": cliente[11],
                "ciudad": cliente[7],
                "Ahorro": cliente[12]
            }
            lista_clientes.append(cliente_dict)
    except Exception as e:
        print(e)
        return []
    finally:
        conexion.close()
        return lista_clientes


@app.get("/clientes/{id}")
async def obtener_cliente_por_id(id: int):
    # Creamos la conexión a la base de datos
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM clientes WHERE id = {id}")
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    cliente = {
    "id": result[0],
    "nombre": result[1],
    "apellido": result[2],
    "fecha de nacimiento": result[3],
    "correo": result[5],
    "direccion": result[6],
    "telefono": result[11],
    "ciudad": result[7],
    "Ahorro": result[12]
    } 
    # Retornamos el diccionario con los datos del cliente
    return cliente

@app.post("/clientes/")
async def crear_cliente(cliente: Cliente):
    conexion = get_database_connection()
    cursor = conexion.cursor()
    insert_query = f"""
        INSERT INTO clientes (nombre, apellido, fecha_nacimiento, genero, correo_electronico, direccion, ciudad, estado, pais, codigo_postal, telefono, saldo_ahorros)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        fecha_nacimiento = datetime.strptime(cliente.fecha_nacimiento, '%Y-%m-%d').date()
        cursor.execute(insert_query, cliente.nombre, cliente.apellido, fecha_nacimiento, cliente.genero, cliente.correo_electronico, cliente.direccion, cliente.ciudad, cliente.estado, cliente.pais, cliente.codigo_postal, cliente.telefono, cliente.saldo_ahorros)
        cursor.commit()
        return {"mensaje": "Cliente creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conexion.close()

@app.put("/clientes/{id}")
async def actualizar_cliente(id: int, cliente: Cliente):
    query = "UPDATE clientes SET nombre=?, apellido=?, telefono=?, correo_electronico=? WHERE id=?"
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(query, (cliente.nombre, cliente.apellido, cliente.telefono, cliente.correo_electronico, id))
        conn.commit()
        return {"message": f"Cliente con ID {id} actualizado exitosamente."}
    except pyodbc.Error as ex:
        print("Error en actualizar_cliente:", ex)
        raise HTTPException(status_code=500, detail="Error del servidor al actualizar el cliente.")
    finally:
        conn.close()

@app.delete("/clientes/{id}")
async def eliminar_cliente(id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    connection.commit()
    return {"mensaje": f"Cliente con id {id} eliminado"}
