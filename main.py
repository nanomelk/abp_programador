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
        print("5. Ver Reporte General")
        print("6. Acerca del Sistema")
        print("7. Salir")

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
                        cuil_cuit = input("Ingrese N° de CUIT o CUIL: ")
                        telefono = input("Telefono: ")
                        email = input("Email: ")
                        print("Cliente registrado con exito")
                        print("Se guardó el cliente, sus datos son: Nombre:", nombre, "CUIL o CUIT", cuil_cuit, "Telefono:", telefono, "Email:", email)           
                        input("presiona enter para salir...")
                elif menuClientes == 3:
                        print("Modificar Cliente")
                        print("Ingrese el CUIL_CUIT del cliente a modificar")
                        "futuro codigo, incluye select y un update"
                        "print('verifique sus datos')"
                        "print('sus datos fueron corregidos correctamente)"                                
                        input("presiona enter para salir...")
                elif menuClientes == 4:
                        print("Borrar Cliente")
                        print("Ingrese el CUIL_CUIT del cliente a borrar")
                        "futuro codigo, incluye select y un delete"
                        "print('Esta seguro que desea eliminar el cliente: CUIT:XXXXXXXXX')"
                        "print('Cliente CUIT:XXXXXXXXXXX correctamente eliminado de la base)"
                        input("presiona enter para salir...")    
                elif menuClientes == 5:
                        break
                else: 
                        print("Opcion Invalida-ingrese una opcion valida")
        elif menu == 2:
            print("You selected Option 2")
            input("Press Enter to continue...")
        elif menu == 3:
            print("Saliendo...")
            break
        elif menu == 6:
            print("\n--- Acerca del Sistema ---")
            print("SkyRoute - Sistema de Gestión de Pasajes")
            print("Versión: 1.0")
            print("Desarrollado por los integrantes del grupo:\n")
            print("- Mechiorre Mariano Sebastián, DNI: 29.252.427")
            print("- Melchorre Alejandra Cristina, DNI: 24.286.870")
            print("- Roque Martín Miguel, DNI: 23.824.997")
            print("- Quispe Christian, DNI: 23.198.068")
            print("- Heredia Joel, DNI: 41.158.023\n")

            print("Descripción:")
            print("Este sistema permite gestionar clientes, destinos y ventas de pasajes,")
            print("incluyendo funcionalidades como consultas, reportes y botón de arrepentimiento.\n")

            print("Derechos de autor:")
            print("© 2025 SkyRoute. Todos los derechos reservados.")
            print("Este software es propiedad exclusiva de los desarrolladores mencionados.")
            print("Queda estrictamente prohibida la copia, distribución, modificación o uso no autorizado")
            print("de este código sin el consentimiento explícito por escrito de los autores.\n")

            input("Presione Enter para volver al menú principal...")
        elif menu == 7:
                print("Esta seguro de salir")
                print("1. Si")
                print("2. No")
                menuSalir = int(input("Elija la opcion: "))
                if menuSalir == 1:
                        print("Saliendo...")
                        break
                elif menuSalir == 2:
                        print("Volviendo al menu principal...")
                else:
                        print("Opcion Invalida-ingrese una opcion valida")
                        input("presiona enter para volver al menu anterior...") 
                
        
if __name__ == "__main__":
    main_menu()