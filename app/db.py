import pyodbc
def get_database_connection():
    ServidorBaseDeDatos = 'LAPTOP-5GLB5BJA\CITADEL'
    NombreDeBaseDeDatos = 'cooperativa'

    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ServidorBaseDeDatos+';DATABASE='+NombreDeBaseDeDatos+';Trusted_Connection=yes')
        print('Conexion exitosa con la bd')
        estadoconexion=True
    except Exception as e:
        print('No se pudo conectar a la bd. Error:', e)
        estadoconexion=False
    return conexion
