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
#
#   Datos de los integrantes del grupo:
#
# - Mechiorre Mariano Sebastián, DNI: 29.252.427
# - Melchorre Alejandra Cristina, DNI: 24.286.870
# - Roque Martín Miguel, DNI: 23.824.997
# - Quispe Christian, DNI 23.198.068
# - Heredia Joel, DNI 41.158.023
#
# ==============================================================================
def main_menu():
    while True:
        """
        1. Gestionar Clientes
        2. Gestionar Destinos
        3. Gestionar Ventas
        4. Consultar Ventas
        5. Botón de Arrepentimiento
        6. Ver Reporte General
        7. Acerca del Sistema
        8. Salir
        """
        print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Botón de Arrepentimiento")
        print("5. Botón de Arrepentimiento")
        print("6. Ver Reporte General")
        print("7. Acerca del Sistema")
        print("8. Salir")

        menu = int(input("Elija la opcion: "))

        if menu == 1:
            while True:
                """
                -- GESTIONAR CLIENTES --
                1. Ver Clientes
                2. Agregar Cliente
                3. Modificar Cliente
                4. Eliminar Cliente
                5. Volver al Menú Principal
                """
                print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
                print("1. Ver Clientes")
                print("2. Agregar Cliente")
                print("3. Modificar Cliente")
                print("4. Eliminar Cliente")
                print("5. Volver al Menú Principal")
                
                menuClientes = int(input("Menu Gestionar Clientes - Elija la opcion: "))
                if menuClientes == 1:
                        print("Lista de Clientes")
                        input("presiona enter para salir...")
                elif menuClientes == 2:
                        print("Ingrese los datos del Nuevo Cliente")
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")
                        fechaNacimiento = input("fecha de Nacimiento: ")
                        telefono = input("Telefono: ")
                        email = input("Email: ")
                        print("Cliente registrado con exito")
                        print("Se guardó el cliente, sus datos son: Nombre:", nombre, "Apellido:", apellido, "fechaNacimiento:", fechaNacimiento, "Telefono:", telefono, "Email:", email)           
                        input("presiona enter para salir...")
                elif menuClientes == 3:
                        print("Modificar Cliente")
                        print("Ingrese el ID del cliente a modificar")
                        input("presiona enter para salir...")
                elif menuClientes == 4:
                        print("Borrar Cliente")
                        print("Ingrese el ID del cliente a borrar")
                        input("presiona enter para salir...")    
                elif menuClientes == 5:
                        break
                else: 
                        print("Opcion Invalida-ingrese una opcion valida")
        elif menu == 2:
            print("You selected Option 2")
            input("Press Enter to continue...")
        elif menu == 3:
            print("Exiting...")
            break
        else:
            print("Opcion Invalida-ingrese una opcion valida")
            input("presiona enter para volver al menu anterior...") 
if __name__ == "__main__":
    main_menu()