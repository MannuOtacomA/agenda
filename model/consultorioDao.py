from model.conexion_db import ConexionDB

# Modelo Consultorio
class Consultorio:
    def __init__(self, nombre, id_hospital=None):
        self.id_consultorio = None
        self.nombre = nombre
        self.id_hospital = id_hospital  # Relación con el hospital

    def __str__(self):
        return f'Consultorio[{self.nombre}, Hospital ID: {self.id_hospital}]'

# Guardar
def guardar(consultorio):
    if not consultorio.nombre or not consultorio.id_hospital:
        #flash("Por favor, completa todos los campos antes de guardar.", "danger")
        return {"status": "danger", "message": "Por favor, completa todos los campos antes de guardar."}

    conexion = ConexionDB()
    sql = '''
    INSERT INTO consultorio (nombre, id_hospital) 
    VALUES (%s, %s)
    '''
    try:
        conexion.cursor.execute(sql, (consultorio.nombre, consultorio.id_hospital))
        conexion.cerrar()
        #flash("Los datos del consultorio se guardaron correctamente.", "success")
        return {"status": "danger", "message": "Los datos del consultorio se guardaron correctamente"}
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo guardar el registro: {e}", "danger")
        return {"status": "danger", "message": "No se pudo guardar el registro: {e}"}

# Listar todos los consultorios
def listar():
    conexion = ConexionDB()
    sql = "SELECT * FROM consultorio"
    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()
        conexion.cerrar()
        return registros
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo recuperar la lista de consultorios: {e}", "danger")
        return [],{"status": "danger", "message": "No se pudo recuperar la lista de consultorios: {e}"}

# Modificar la función listar para incluir el nombre del hospital
def listar_con_nom_hos():
    conexion = ConexionDB()
    sql = '''
    SELECT consultorio.id_consultorio, consultorio.nombre, hospital.nombre AS hospital_nombre
    FROM consultorio
    JOIN hospital ON consultorio.id_hospital = hospital.id_hospital
    '''
    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()
        conexion.cerrar()
        return registros
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo recuperar la lista de consultorios: {e}", "danger")
        return [],{"status": "danger", "message": "No se pudo recuperar la lista de consultorios: {e}"}


# Listar todos los hospitales  para llenar combo
def listar_h_id_nom():
    conexion = ConexionDB()
    sql = "SELECT id_hospital, nombre FROM hospital"
    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()
        conexion.cerrar()
        return registros
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo recuperar la lista de consultorios: {e}", "danger")
        return [],{"status": "danger", "message": "No se pudo recuperar la lista de consultorios: {e}"}

# Listar un consultorio por ID
def listar_por_id(id_consultorio):
    conexion = ConexionDB()
    sql = "SELECT * FROM consultorio WHERE id_consultorio = %s"
    try:
        conexion.cursor.execute(sql, (id_consultorio,))
        registro = conexion.cursor.fetchone()  # Esperamos un único resultado
        conexion.cerrar()

        if registro:
            return registro
        else:
            return None
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo recuperar la lista de consultorios: {e}", "danger")
        return None, {"status": "danger", "message": "No se pudo recuperar la lista de consultorios: {e}"}

# Editar un consultorio
def editar(consultorio, id_consultorio):
    conexion = ConexionDB()
    sql = '''
    UPDATE consultorio 
    SET nombre = %s, id_hospital = %s
    WHERE id_consultorio = %s
    '''
    try:
        conexion.cursor.execute(sql, (consultorio.nombre, consultorio.id_hospital, id_consultorio))
        conexion.cerrar()
        #flash("El registro se actualizó correctamente.", "success")
        return {"status": "danger", "message": "El registro se actualizó correctamente."}
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo editar el registro: {e}", "danger")
        return {"status": "danger", "message": "No se pudo editar el registro: {e}"}

# Eliminar un consultorio
def eliminar(id_consultorio):
    conexion = ConexionDB()
    sql = "DELETE FROM consultorio WHERE id_consultorio = %s"
    try:
        conexion.cursor.execute(sql, (id_consultorio,))
        conexion.cerrar()
       #flash("El registro se eliminó correctamente.", "success")
        return {"status": "danger", "message": "El registro se eliminó correctamente."}
    except Exception as e:
        conexion.cerrar()
        #flash(f"No se pudo eliminar el registro: {e}", "danger")
        return {"status": "danger", "message": "No se pudo eliminar el registro: {e}"}
