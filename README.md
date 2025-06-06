# ✈️ SkyRoute - Sistema de Gestión de Pasajes

**Repositorio del Proyecto**:  
🔗 [https://github.com/nanomelk/abp_programador.git](https://github.com/nanomelk/abp_programador.git)

## 👥 Integrantes del Grupo

- **Mechiorre Mariano Sebastián** - DNI: 29.252.427   
- **Roque Martín Miguel** - DNI: 23.824.997  
- **Quispe Christian** - DNI: 23.198.068  
- **Heredia Joel** - DNI: 41.158.023  

---

## 📌 Descripción del Proyecto

SkyRoute es una aplicación de consola desarrollada en Python para simular el funcionamiento básico de un sistema de gestión de pasajes. Permite realizar operaciones sobre clientes, destinos y ventas, incluyendo la funcionalidad legal del botón de arrepentimiento.

Este sistema está orientado a brindar una solución simple pero robusta a una empresa ficticia de viajes, e incluye conexión a una base de datos MySQL para persistencia de los datos.

---

## ⚙️ Estructura del Proyecto

skyroute/ <br>
├── config.py # Configuración de la base de datos <br>
├── conexion_base_datos.py # Módulo de conexión MySQL  (Funciones: crear_Conexion() y cerrar_conexion() )<br>
├── gestion_clientes.py # Funcionalidades y menú de clientes <br>
├── gestion_destinos.py # Funcionalidades y menú de destinos <br>
├── gestion_ventas.py # Funcionalidades y menú de ventas y botón de arrepentimiento <br>
├── main.py # Menú principal <br>
├── DER.sql # Script SQL con DDL y DML comentado <br>
├── README.md # Este archivo <br>

---

## 🚀 Funcionalidades del Sistema

### 1. Gestión de Clientes
- Agregar cliente (razón social, CUIT, email)
- Listar clientes registrados
- Modificar cliente
- Eliminar cliente

### 2. Gestión de Destinos
- Registrar destino (ciudad, descripción, precio, noches)
- Listar destinos
- Modificar destino
- Eliminar destino

### 3. Gestión de Ventas
- Registrar venta (cliente, destino, fecha y costo)
- Estado de la venta: "Activa" o "Anulada"

### 4. Botón de Arrepentimiento
- Anular ventas dentro de los primeros 60 días desde la compra
- Rechazar anulaciones si faltan menos de 72h para la salida
- Cambio automático del estado de la venta a "Anulada"

---

## 🧠 Contenidos de Programación Aplicados

- Modularización de código (funciones y archivos separados)
- Estructuras de control (`if`, `while`, `for`)
- Listas y diccionarios
- Conexión a MySQL con `mysql.connector`
- Uso de fechas con `datetime`
- Git y GitHub para control de versiones

---

## 💾 Base de Datos

Se implementó una base de datos relacional en MySQL que incluye:

### Tablas creadas:
- `clientes`  
- `destinos`  
- `estado`  
- `ventas`  

### Script SQL:
El archivo `estructura_y_datos.sql` incluye:
- Sentencias DDL (creación de tablas, claves primarias y foráneas)
- Sentencias DML para poblar datos (mínimo 3 registros por tabla)
- 5 consultas SQL de ejemplo:
  - Listar todos los clientes
  - Ventas en una fecha específica
  - Última venta por cliente
  - Destinos que empiezan con “S”
  - Cantidad de ventas por ciudad
** Ejemplos Adjuntos en DER.sql

---

## 🧾 Aspectos Éticos y Legales

### Ley 11.723 - Propiedad Intelectual
ROCKET SAS (grupo desarrollador) retiene la propiedad intelectual del código, otorgando licencia de uso a SkyRoute S.R.L.

### Ley 25.326 - Protección de Datos Personales
Los datos de los clientes son gestionados bajo la figura de "responsable del tratamiento", cumpliendo la legislación vigente.

### Botón de Arrepentimiento
Se implementa conforme a las leyes 24.240 y 26.994, permitiendo la anulación de una compra dentro de los primeros 60 días, salvo que falten menos de 72h para el viaje.

### Convenio de Budapest (cibercrimen)
Si el sistema se implementa en España y ocurre un incidente desde Argentina, se aplican los principios de cooperación internacional y jurisdicción cruzada según el tratado.

### Inteligencia Artificial
Si se integrara IA en el futuro, se seguiría la Ley N° 27.701 (Argentina) y regulaciones europeas como el **AI Act**, además de aplicar principios éticos como transparencia, no discriminación y protección de datos.

---

## ▶️ Instrucciones de Ejecución

1. Tener instalado Python 3.x
2. Clonar el repositorio:
git clone https://github.com/nanomelk/abp_programador.git

3. Iniciar el programa:
cd abp_programador
python main.py

---

## 🧪 Pruebas y Validaciones

- Todos los módulos fueron testeados localmente con conexión MySQL activa.
- Se validó el botón de arrepentimiento con fechas límite simuladas.
- Se corroboró que no se puede anular una venta si pasaron más de 60 días (con un escala a 60 segundos) o si faltan menos de 72h para la salida.

---

## 🎥 Video de Presentación

➡️ Video en el que todos los integrantes comentan brevemente:
- Organización del grupo
- Dificultades encontradas
- Qué les gustó del proyecto
- Qué mejorarían
- Temas en los que necesitan más práctica

*(Link al video se incluirá al momento de la entrega)*

---

## 🧾 Poster del Proyecto

Ver archivo `Poster_ABP_2025.pdf` incluido en el repositorio.

---

## 📎 Archivos incluidos para entrega

- Código fuente completo (`.py`)
- Script SQL (`DER.sql`)
- Documento de Ética (`ABP_ETICA_2da_entrega.pdf`)
- README actualizado
- Poster oficial

---

*¡Gracias por revisar nuestro proyecto!*