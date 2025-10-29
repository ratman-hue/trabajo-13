# Empleado.py

# Importa la clase de conexión del módulo anterior
from ConexionDB import ConexionDB 

class Empleado:
    """Clase que representa el modelo de datos de un empleado (POO)."""
    def __init__(self, nombre, sexo, correo, id=None):
        self.id = id # Se recibirá después de la inserción o al consultar
        self.nombre = nombre
        self.sexo = sexo
        self.correo = correo

class EmpleadoManager:
    """Clase que maneja las operaciones CRUD de los empleados con la base de datos."""
    def __init__(self, db_manager):
        self.db = db_manager

    def agregar_empleado(self, empleado):
        """Añadir empleado[cite: 14]. Retorna True si es exitoso."""
        query = "INSERT INTO empleados (nombre, sexo, correo) VALUES (%s, %s, %s)"
        params = (empleado.nombre, empleado.sexo, empleado.correo)
        return self.db.execute_query(query, params)

    def ver_empleados(self):
        """Ver empleados[cite: 13]. Retorna una lista de objetos Empleado."""
        query = "SELECT id, nombre, sexo, correo FROM empleados ORDER BY id DESC"
        results = self.db.execute_query(query, fetch=True)
        if results:
            # Mapea los resultados de la DB a una lista de objetos Empleado
            return [Empleado(r[1], r[2], r[3], r[0]) for r in results]
        return []

    def eliminar_empleado(self, empleado_id):
        """Eliminar empleado[cite: 19]. Retorna True si es exitoso."""
        query = "DELETE FROM empleados WHERE id = %s"
        params = (empleado_id,)
        return self.db.execute_query(query, params)