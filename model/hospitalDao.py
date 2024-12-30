from model.conexion_db import ConexionDB


def crear_tabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE IF NOT EXISTS hospital (
        id_hospital SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        direccion VARCHAR(100) NOT NULL,
        telefono VARCHAR(50) NOT NULL
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        return {"status": "success", "message": "Se creó la tabla en la base de datos PostgreSQL."}
    except Exception as e:
        conexion.cerrar()
        return {"status": "danger", "message": f"No se pudo crear la tabla: {e}"}

def boorar_tabla():
    conexion = ConexionDB()
    sql = "DROP TABLE hospital"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        return {"status": "success", "message": "Se borró la tabla en la base de datos."}
    except Exception as e:
        return {"status": "warning", "message": "No existe tabla para borrar."}

#modelo hospital
class Hospital():
    def __init__(self, nombre,direccion,telefono):
        self.id_hospital = None
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f'Hospital[{self.nombre},{self.direccion},{self.telefono}]'

#guardar
def guardar(hospital):
    conexion = ConexionDB()
    sql = '''
    INSERT INTO hospital (nombre, direccion, telefono) 
    VALUES (%s, %s, %s)
    '''
    try:
        conexion.cursor.execute(sql, (hospital.nombre, hospital.direccion, hospital.telefono))
        conexion.cerrar()
        return {"status": "success", "message": "Los datos del hospital se guardaron correctamente."}
    except Exception as e:
        conexion.cerrar()
        return {"status": "danger", "message": f"No se pudo guardar el registro: {e}"}

#listar
def listar_hospital():
    conexion = ConexionDB()
    sql = "SELECT * FROM hospital"
    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()
        conexion.cerrar()
        return registros
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo recuperar la lista de hospitales: {e}", "danger")
        return [], {"status": "warning", "message": "No se pudo recuperar la lista de hospitales: {e}"}


#listar por id
def listar_por_id(id_hospital):
    conexion = ConexionDB()
    sql = "SELECT * FROM hospital WHERE id_hospital = %s"  # Ajustamos la consulta para buscar por id
    try:
        conexion.cursor.execute(sql, (id_hospital,))
        registro = conexion.cursor.fetchone()
        conexion.cerrar()
        if registro:
            return registro
        else:
            return None, {"status": "warning", "message": "No se encontró el hospital."}
    except Exception as e:
        conexion.cerrar()
        return None, {"status": "danger", "message": f"No se pudo recuperar el hospital con ID {id_hospital}: {e}"}


#actualizar
def editar(hospital, id_hospital):
    conexion = ConexionDB()
    sql = '''
    UPDATE hospital 
    SET nombre = %s, direccion = %s, telefono = %s
    WHERE id_hospital = %s
    '''
    try:
        conexion.cursor.execute(sql, (hospital.nombre, hospital.direccion, hospital.telefono, id_hospital))
        conexion.cerrar()
        return {"status": "success", "message": "El registro se actualizó correctamente."}
    except Exception as e:
        conexion.cerrar()
        return {"status": "danger", "message": f"No se pudo editar el registro: {e}"}


#eliminar
def eliminar(id_hospital):
    conexion = ConexionDB()
    sql = "DELETE FROM hospital WHERE id_hospital = %s"
    try:
        conexion.cursor.execute(sql, (id_hospital,))
        conexion.cerrar()
        return {"status": "success", "message": "El registro se eliminó correctamente."}
    except Exception as e:
        conexion.cerrar()
        return {"status": "danger", "message": f"No se pudo eliminar el registro: {e}"}




