import conexion_base_datos as db


def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Agregar Cliente")
        print("2. listar Clientes registrados")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        try:
            menu = int(input("Elija una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if menu == 1:
            print("Agregar Nuevo Cliente, PRESTE ATENCIÓN A LOS DATOS")
            razon_social = input("Nombre/Razón Social: ")
            cuit = input("CUIL/CUIT: ")
            email = input("Email: ")

            conexion = db.crear_conexion()
            cursor = conexion.cursor()
            sqlNuevoCliente = (
                "INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)"
            )
            cursor.execute(sqlNuevoCliente, (razon_social, cuit, email))
            conexion.commit()
            cursor.close()
            db.cerrar_conexion(conexion)

            print(f"Cliente {razon_social} registrado con éxito.")
            input("Presione Enter para continuar...")
        elif menu == 2:
            conn = db.crear_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM clientes")
            clientes = cur.fetchall()

            if clientes:
                print("\nLista de Clientes:")
                for c in clientes:
                    print(f"Razón Social:{c[1]} - CUIT/CUIL:{c[0]} - email:{c[2]}")
            else:
                print("No se encontraron clientes.")

                cursor.close()
                db.cerrar_conexion(conexion)
                input("Presione Enter para continuar...")
        elif menu == 3:
            cuit = input("Ingrese el CUIT/CUIL del cliente a modificar: ")
            conn = db.crear_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM clientes where cuit = %s", (cuit,))
            cliente = cur.fetchone()
            if not cliente:
                print(f"No se encontró un cliente con CUIT/CUIL {cuit}.")
                input("Presione Enter para continuar...")
                continue
            else:
                print(f"Cliente encontrado: {cliente[1]} - {cliente[0]} - {cliente[2]}")
                razon_social = input("Ingrese el nuevo nombre/razón social: ")
                email = input("Ingrese el nuevo email: ")
            print("Modificando cliente...")
            sqlModificarCliente = (
                "UPDATE clientes SET razon_social = %s, email = %s WHERE cuit = %s"
            )
            cur.execute(sqlModificarCliente, (razon_social, email, cuit))
            conn.commit()
            cur.close()
            db.cerrar_conexion(conn)

            print(f"Cliente con CUIT/CUIL {cuit} modificado con éxito.")
            input("Presione Enter para continuar...")
        elif menu == 4:
            cuit = input("Ingrese el CUIT/CUIL del cliente a eliminar: ")
            conn = db.crear_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
            cliente = cur.fetchone()
            if not cliente:
                print(f"No se encontró un cliente con CUIT/CUIL {cuit}.")
                input("Presione Enter para continuar...")
                continue
            else:
                print(f"Cliente encontrado: {cliente[1]} - {cliente[0]} - {cliente[2]}")
                confirmacion = input("¿Está seguro de eliminar este cliente? (s/n): ")
                if confirmacion.lower() == "s":
                    sqlEliminarCliente = "DELETE FROM clientes WHERE cuit = %s"
                    cur.execute(sqlEliminarCliente, (cuit,))
                    conn.commit()
                    print(f"Cliente con CUIT/CUIL {cuit} eliminado con éxito.")
                else:
                    print("Operación cancelada.")
            cur.close()
            db.cerrar_conexion(conn)
            input("Presione Enter para continuar...")

        elif menu == 5:
            break
