import data.database as db


def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        try:
            menu = int(input("Elija una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if menu == 2:
            print("Agregar Nuevo Cliente, PRESTE ATENCIÓN A LOS DATOS")
            razon_social = input("Nombre/Razón Social: ")
            cuit_cuil = input("CUIL/CUIT: ")
            email = input("Email: ")

            conexion = db.crear_conexion()
            cursor = conexion.cursor()
            sqlNuevoCliente = "INSERT INTO clientes (razon_social, cuit_cuil, correo_electronico) VALUES (%s, %s, %s)"
            cursor.execute(sqlNuevoCliente, (razon_social, cuit_cuil, email))
            conexion.commit()
            cursor.close()
            db.cerrar_conexion(conexion)

            print(f"Cliente {razon_social} registrado con éxito.")
            input("Presione Enter para continuar...")

        # El resto de opciones...

        elif menu == 5:
            break
