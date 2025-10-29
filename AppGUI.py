# AppGUI.py

import tkinter as tk
from tkinter import ttk, messagebox
# Importa la lógica de los otros módulos
from ConexionDB import ConexionDB, crear_tabla_empleados 
from Empleado import Empleado, EmpleadoManager

class AppGUI(tk.Frame):
    """Aplicación principal que hereda de tk.Frame, usando POO."""
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(sticky="nsew")

        # --- CONFIGURACIÓN DE DB Y MANAGER ---
        # ATENCIÓN: Reemplaza "tu_contraseña" por la real
        self.db = ConexionDB(
            host="localhost", 
            database="registro_empleados", 
            user="root", 
            password="toor" 
        )
        crear_tabla_empleados(self.db) 
        self.manager = EmpleadoManager(self.db)
        
        # --- CREACIÓN DE LA GUI ---
        self.createWidgets()
        self.cargar_empleados()

    def createWidgets(self):
        # Configuración del Notebook (Pestañas para separar la lógica de la GUI)
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Pestaña 1: Añadir Empleado
        frame_registro = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame_registro, text=' ➕ Añadir Empleado ')
        self._create_registro_form(frame_registro)

        # Pestaña 2: Ver/Eliminar Empleados
        frame_listado = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame_listado, text=' 📋 Ver/Eliminar Empleados ')
        self._create_listado_table(frame_listado)

        # Permite que la ventana principal se redimensione
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_registro_form(self, frame):
        """Crea el formulario para Añadir Empleado."""
        
        # Nombre [cite: 15]
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(frame, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Sexo [cite: 16]
        ttk.Label(frame, text="Sexo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.sexo_var = tk.StringVar(value='Masculino')
        radio_frame = ttk.Frame(frame)
        radio_frame.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(radio_frame, text="Masculino", variable=self.sexo_var, value="Masculino").pack(side="left", padx=10)
        ttk.Radiobutton(radio_frame, text="Femenino", variable=self.sexo_var, value="Femenino").pack(side="left")
        
        # Correo [cite: 17]
        ttk.Label(frame, text="Correo:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_correo = ttk.Entry(frame, width=40)
        self.entry_correo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Botón de Añadir Empleado [cite: 14]
        self.btn_anadir = ttk.Button(frame, text="Añadir Empleado", command=self.anadir_empleado)
        self.btn_anadir.grid(row=3, column=0, columnspan=2, pady=20)
        frame.grid_columnconfigure(1, weight=1)


    def _create_listado_table(self, frame):
        """Crea la tabla (Treeview) para Ver y Eliminar Empleados."""
        
        columns = ("id", "nombre", "sexo", "correo")
        self.tree = ttk.Treeview(frame, columns=columns, show='headings', height=10)
        
        # Encabezados
        self.tree.heading("id", text="ID (Auto)") # ID Generado Automáticamente [cite: 18]
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("sexo", text="Sexo")
        self.tree.heading("correo", text="Correo")
        
        # Dimensiones
        self.tree.column("id", width=60, anchor="center")
        self.tree.column("nombre", width=180)
        self.tree.column("sexo", width=90, anchor="center")
        self.tree.column("correo", width=250)

        self.tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Botón de Eliminar Empleado [cite: 19]
        self.btn_eliminar = ttk.Button(frame, text="Eliminar Empleado Seleccionado", command=self.eliminar_empleado) 
        self.btn_eliminar.grid(row=1, column=0, columnspan=2, pady=10)
        
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)


    # --- Métodos de Interacción (Lógica) ---

    def cargar_empleados(self):
        """Carga los empleados de la DB y actualiza el Treeview (Ver empleados [cite: 13])."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        empleados = self.manager.ver_empleados()
        for emp in empleados:
            self.tree.insert('', tk.END, values=(emp.id, emp.nombre, emp.sexo, emp.correo))

    def anadir_empleado(self):
        """Procesa el formulario para Añadir empleado[cite: 14]."""
        nombre = self.entry_nombre.get().strip()
        sexo = self.sexo_var.get()
        correo = self.entry_correo.get().strip()

        if not nombre or not correo:
            messagebox.showerror("Error", "Nombre y Correo no pueden estar vacíos.")
            return

        nuevo_empleado = Empleado(nombre, sexo, correo)
        
        if self.manager.agregar_empleado(nuevo_empleado):
            messagebox.showinfo("Éxito", "Empleado añadido correctamente.")
            self.entry_nombre.delete(0, tk.END)
            self.entry_correo.delete(0, tk.END)
            self.cargar_empleados()
            self.notebook.select(1) # Ir a la pestaña de listado

    def eliminar_empleado(self):
        """Procesa la eliminación del empleado seleccionado[cite: 19]."""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar.")
            return

        # Obtenemos el ID de la primera columna (es clave para la eliminación)
        empleado_id = self.tree.item(selected_item, 'values')[0]
        
        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar al ID: {empleado_id}?"):
            if self.manager.eliminar_empleado(empleado_id):
                messagebox.showinfo("Éxito", "Empleado eliminado.")
                self.cargar_empleados()
            

# --- Bloque de Ejecución Principal ---

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Registro de Empleados | POO + Tkinter + MySQL')
    
    # Configuración de la ventana principal
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    app = AppGUI(master=root)
    app.mainloop()