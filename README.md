# ⚙️ Sistema de Registro de Empleados (POO + Tkinter + MySQL)

## 🎯 Objetivo del Proyecto

Este proyecto es la solución a la actividad de crear un sistema completo de **Registro de Empleados** utilizando el paradigma de **Programación Orientada a Objetos (POO)** en Python, con una Interfaz Gráfica de Usuario (GUI) desarrollada con **Tkinter**, y persistencia de datos mediante una conexión a **MySQL**.

El sistema cumple con todos los requisitos funcionales y de arquitectura solicitados en la actividad.

## ✨ Funcionalidades Implementadas

El sistema permite la gestión completa de los registros de empleados:

* **Ver Empleados:** Muestra una lista actualizada de todos los empleados registrados en la base de datos, incluyendo su **ID Generado Automáticamente**.
* **Añadir Empleado:** Permite ingresar el **Nombre**, **Sexo** y **Correo** del empleado.
* **Eliminar Empleado:** Permite seleccionar y eliminar registros directamente desde la interfaz.
* **Conexión con MySQL:** Utiliza el conector oficial de Python para interactuar con la base de datos.

## 🛠️ Arquitectura y Mejoras Clave

La arquitectura de este proyecto fue diseñada para cumplir con la necesidad de tener un código **modular, legible y escalable**.

| Requisito de la Actividad | Implementación y Mejora | Archivo(s) Correspondiente(s) |
| :--- | :--- | :--- |
| **POO** | Toda la lógica está encapsulada en clases, garantizando la correcta aplicación del paradigma. | `ConexionDB.py`, `Empleado.py`, `AppGUI.py` |
| **Código Modular** | El proyecto está dividido en tres archivos lógicos, separando la capa de datos, el modelo de negocio y la interfaz de usuario. | `ConexionDB.py`, `Empleado.py`, `AppGUI.py` |
| **Consultas Seguras** | Se utiliza la **parametrización de consultas** (`%s`) en la clase `ConexionDB` para prevenir ataques de inyección SQL. | `ConexionDB.py` |
| **Interfaz Amigable** | Se utiliza un **`ttk.Notebook` (pestañas)** para organizar la vista de registro (`Añadir`) y la vista de datos (`Ver/Eliminar`). | `AppGUI.py` |

## ⚙️ Estructura del Código

El proyecto consta de los siguientes módulos:

1.  **`ConexionDB.py`:** Maneja la conexión segura y las consultas a la base de datos MySQL.
2.  **`Empleado.py`:** Define el modelo `Empleado` y la lógica de negocio (CRUD) en `EmpleadoManager`.
3.  **`AppGUI.py`:** Contiene la interfaz gráfica de Tkinter y enlaza las acciones del usuario con la lógica del negocio.

## 🚀 Cómo Ejecutar

### Requisitos

* Python 3.x
* Servidor MySQL en funcionamiento.

### Instalación de Dependencias

```bash
pip install mysql-connector-python ```

Configuración de la Base de Datos
Crea la base de datos: CREATE DATABASE registro_empleados;

Modifica los archivos ConexionDB.py y AppGUI.py y reemplaza "root" con tu contraseña real de MySQL.

Ejecución
El script principal a ejecutar es AppGUI.py:

``` bash
python AppGUI.py ```
