
def main_menu():
    while True:
        print("Menu principal: SKYRoute.SRL")
        print("1. Clientes")
        print("2. Pasajes")
        print("3. Exit")


        menu = int(input("Elija la opcion: "))

        if menu == 1:
            while True:
                print("You selected Option 1")
                print("Main Menu:")
                print("1. Nuevo Cliente")
                print("2. Lista de Clientes")
                print("2. Modificar Cliente")
                print("3. Borrar Cliente")
                print("3. Exit")
                menuClientes = int(input("Elija la opcion: "))
                if menuClientes == 1:
                        print("Ingrese los datos del nuevo cliente")
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")
                        edad = input("Edad: ")
                        telefono = input("Telefono: ")
                        email = input("Email: ")
                        print("Cliente registrado con exito")
                        print("Nombre:", nombre, "Apellido:", apellido, "Edad:", edad, "Telefono:", telefono, "Email:", email)           
                        input("presiona enter para salir...")
                        break
                elif menuClientes == 2:
                        print("You selected Option 2")
                        input("presiona enter para salir...")
                elif menuClientes == 3:
                        print("Exiting...")
                        break
                else: 
                        print("Invalid choice. Please try again.")
                        input("presiona enter para salir...")
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