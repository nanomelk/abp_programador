# ==============================================================================
# Propósito del Sistema:
#
# Este programa es una aplicacion por consola funcionamiento básico de un sistema
# de gestión de pasajes de una empresa SkyRoute. El objetivo es permitir
# gestionar clientes, destinos y ventas de pasajes. El sistema premite registrar
#  clientes y destinos, ventas, visualizarlas, modificarlas y eliminarlas, mediante el botón de
# arrepentimiento. El sistema también permite ademas consultar ventas y generar reportes,
# mediante una funcionalidad de "botón de arrepentimiento".
# El proyecto final utilizará una base de datos relacional para la persistencia
# de los datos.
#
# Cómo instalar y ejecutar el programa:
#
# Para instalar y ejecutar este programa, siga los siguientes pasos:
#
# 1.  Instalar Python:
#     Este programa requiere tener instalado el intérprete de Python (se
#     recomienda la versión más reciente compatible con su sistema operativo).
#     a. Descargue el instalador desde el sitio oficial: Python.org
#     b. Ejecute el instalador. Es **importante** seleccionar la opción para
#        "Agregar Python al PATH del sistema" durante la instalación.
#     c. Verifique la instalación abriendo una terminal o línea de comandos
#        y ejecutando el comando: `py --version` (o `python --version`
#        o `python3 --version`, dependiendo de su sistema operativo).
#        Debería ver la versión de Python instalada.
#
# 2.  Obtener el archivo del programa:
#     Obtenga el archivo `main.py` que contiene el código fuente del prototipo.
#     Esto puede ser descargando el archivo directamente o clonando el repositorio
#     de https://github.com/nanomelk/abp_programador.git.
#
# 3.  Ejecutar el programa:
#     a. Abra una terminal o línea de comandos.
#     b. Navegue hasta la carpeta donde se encuentra el archivo `main.py`.
#        Puede usar el comando `cd` (Change Directory).
#     c. Ejecute el script de Python utilizando el comando del intérprete:
#        `python main.py` (o `python3 main.py` si es el comando para su instalación) [17].
#     d. El programa se iniciará y debería mostrar un menú de opciones
#        en la consola [11]. Interactúe con el programa seleccionando las
#        opciones del menú.
# |
#   Datos de los integrantes del grupo:
#
# - Melchiorre Mariano Sebastián, DNI: 29.252.427
# - Roque Martín Miguel, DNI: 23.824.997
# - Quispe Christian, DNI 23.198.068
# - Heredia Joel, DNI 41.158.023
#
# ==============================================================================
from gestion_clientes import gestionar_clientes
from gestion_destinos import gestionar_destinos
from gestion_ventas import boton_arrepentimiento, menu_ventas
from reportes_menu import mostrar_acerca_de
from conexion_base_datos import crear_conexion, cerrar_conexion


def main_menu():
    while True:
        print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Botón de Arrepentimiento")
        print("5. Ver Reporte General")
        print("6. Acerca del Sistema")
        print("7. Salir")

        menu = int(input("Elija la opción: "))

        if menu == 1:
            gestionar_clientes()
        elif menu == 2:
            gestionar_destinos()
        elif menu == 3:
            print("Compras de paquetes de viajes, PRESTE ATENCIÓN A LOS DATOS")
            menu_ventas()
        elif menu == 4:
            boton_arrepentimiento()
        elif menu == 5:
            print("Aquí irán los reportes generales. (Funcionalidad pendiente)")
            input("Presiona Enter para continuar...")
        elif menu == 6:
            mostrar_acerca_de()
        elif menu == 7:
            salir = int(input("¿Está seguro de salir? (1. Sí / 2. No): "))
            if salir == 1:
                print("Saliendo...")
                break
            else:
                print("Volviendo al menú principal...")
        else:
            print("Opción inválida")


if __name__ == "__main__":
    conexion = crear_conexion()  # Intentamos conectar a la base
    if conexion:
        try:
            main_menu()
        finally:
            cerrar_conexion(conexion)  # Nos aseguramos de cerrarla siempre
