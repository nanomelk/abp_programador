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
- (el sistema escala los dias en min, por lo que despues de 60 min,
-  no se puede anular la compra con el botón de arrepentimeinto)
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
El archivo `DER.sql` incluye:
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

# 🧾 Consideraciones Éticas y Legales

Este proyecto no solo aborda aspectos técnicos, sino también los aspectos legales y éticos relacionados con el desarrollo del software para la empresa ficticia **SkyRoute S.R.L.**, conforme a la legislación vigente en Argentina.

### 📘 Aplicación de la Ley 11.723 - Propiedad Intelectual

El código fuente del sistema desarrollado está protegido por la **Ley 11.723**, que regula los derechos de autor en Argentina, incluyendo expresamente a los programas de computación.

#### 1. Reconocimiento de autoría y coautoría

Este proyecto fue desarrollado en equipo. La coautoría está documentada en el encabezado de cada archivo fuente y en este `README.md`:

> **Sistema de Gestión de Pasajes Aéreos - SkyRoute S.R.L.**  
> **Autores**: Mariano Sebastián Mechiorre, Martín Miguel Roque, Christian Quispe, Joel Heredia **El código fuente** es propiedad intelectual de **ROCKET SAS**
> **Fecha de creación**: junio 2025  
> **Protegido por la Ley 11.723 de Propiedad Intelectual, Argentina**

#### 2. Registro del software

Antes de su entrega al cliente se registrará la propiedad intelectual en la **Dirección Nacional del Derecho de Autor (DNDA)** presentando el código fuente y la documentación técnica. Este registro actúa como prueba legal de autoría y fecha de creación en caso de conflictos.

#### 3. Establecimiento de una licencia de uso

> **Este software fue desarrollado con fines académicos. Todos los derechos están reservados a los autores según la Ley 11.723. No se permite su uso, distribución o modificación sin autorización expresa.**

Si en el futuro se decide compartir el código públicamente, podrá aplicarse una licencia de software libre apropiada, respetando siempre la autoría original.

#### 4. Conservación de evidencias

Durante el desarrollo del sistema se utilizó **GitHub** como sistema de control de versiones, registrando cada modificación en el código. También se conservaron diagramas, documentación técnica y decisiones del equipo, lo que constituye evidencia válida en caso de disputas legales.

---

### 🛡️ Aplicación de la Ley 25.326 - Protección de Datos Personales

La base de datos del sistema fue diseñada cumpliendo con los principios de la **Ley 25.326** que regula el uso de datos personales en Argentina.

#### 🔐 Medidas adoptadas:

- **Consentimiento informado**: El sistema contempla incluir (en futuras versiones) una aceptación expresa del cliente sobre el uso de sus datos.
- **Minimización de datos**: Solo se almacena la información necesaria (CUIT, razón social, email). No se solicitan datos sensibles innecesarios.
- **Finalidad del uso**: Los datos solo se usan para gestionar reservas y ventas de pasajes. No se usan para fines comerciales ni se comparten con terceros.
- **Seguridad**: Se restringirá el acceso a los datos a través de autenticación, y se contemplan medidas futuras como encriptación.

---

### ⚖️ Estructura Legal del Grupo

#### 🔹 Figura legal: Sociedad por Acciones Simplificada (SAS)

El grupo adopta la figura de **ROCKET SAS**, una **SAS** que brinda agilidad, protección patrimonial y capacidad de escalar el emprendimiento a futuro.

#### 🔹 Relación con SkyRoute S.R.L.

Se establece mediante un **contrato de licencia de uso**, donde:

- **ROCKET SAS mantiene la propiedad del software.**
- **SkyRoute S.R.L. obtiene el derecho de uso.** mientras que persista soporte técnico y mantenimiento, generando una relación comercial continua.

#### 🔹 En caso de cambio de proveedor

Si SkyRoute decide cambiar de equipo proveedor:

- ROCKET SAS, como persona jurídica, actúa según lo estipulado en el contrato.
- Se aplican cláusulas de rescisión y comunicación formal.
- Los integrantes actúan profesionalmente para proteger los intereses de la sociedad.

#### 🔹 Propiedad de los datos y del código

- **Los datos del sistema** son propiedad de **SkyRoute S.R.L.**, quien actúa como “responsable del tratamiento” según la Ley 25.326.
- **El código fuente** es propiedad intelectual de **ROCKET SAS**, conforme a la Ley 11.723.

#### 🔹 Botón de Arrepentimiento

Implementado según las **Leyes 24.240 y 26.994**, el botón permite anular una compra si:
- No pasaron más de **60 días** desde la venta.
- Faltan más de **72 horas** para la salida del viaje.

Esto asegura los derechos del consumidor conforme a la legislación argentina vigente.

---

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

Video disponible en:
https://www.youtube.com/watch?v=M_ipnPU9k9U 

---

## 🧾 Poster del Proyecto

Ver archivo `Defensa en el Proyecto - ABP.png` incluido en el repositorio.

---

## 📎 Archivos incluidos para entrega

- Código fuente completo (`.py`)
- Script SQL (`DER.sql`)
- Documento de Ética (`ABP_ETICA_2da_entrega.pdf`)
- Regimen Legal de la Propiedad Intelectual.docx (Este amplía la informacion de este Readme)
- README actualizado
- Poster oficial

---

*¡Gracias por revisar nuestro proyecto!*
