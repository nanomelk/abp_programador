
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
                        break
                elif menuClientes == 2:
                        print("Ingrese los datos del Nuevo Cliente")
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")
                        fechaNacimiento = input("fecha de Nacimiento: ")
                        telefono = input("Telefono: ")
                        email = input("Email: ")
                        print("Cliente registrado con exito")
                        print("Nombre:", nombre, "Apellido:", apellido, "fechaNacimiento:", fechaNacimiento, "Telefono:", telefono, "Email:", email)           
                        input("presiona enter para salir...")
                        break
                elif menuClientes == 3:
                        print("Modificar Cliente")
                        print("Ingrese el ID del cliente a modificar")
                        input("presiona enter para salir...")
                elif menuClientes == 4:
                        print("Borrar Cliente")
                        print("Ingrese el ID del cliente a borrar")
                        input("presiona enter para salir...")    
                elif menuClientes == 5:
                        input("presiona enter para salir...")
                        break
                else: 
                        print("Opcion Invalida-ingrese una opcion valida")
                        break
        elif menu == 2:
            print("You selected Option 2")
            input("Press Enter to continue...")
        elif menu == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()