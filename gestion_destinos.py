import conexion_base_datos as db


def gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Registrar Destino")
        print("2. Listar Destinos disponibles")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")

        try:
            menu = int(input("Elija una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if menu == 1:
            print("Agregar Nuevo Destino, PRESTE ATENCIÓN A LOS DATOS")
            ciudad = input("Cuidad del Destino: ")
            descripcion = input("Descripción: ")
            precio_noche = input("Precio Noche: ")
            noches = input("Cantidad de Noches: ")
            conexion = db.crear_conexion()
            cursor = conexion.cursor()
            sqlNuevoDestino = "INSERT INTO destinos (ciudad, descripcion, precio_noche, noches) VALUES (%s, %s, %s, %s)"
            cursor.execute(sqlNuevoDestino, (ciudad, descripcion, precio_noche, noches))
            conexion.commit()
            cursor.close()
            db.cerrar_conexion(conexion)

            print(f"Destino {descripcion} registrado con éxito.")
            input("Presione Enter para continuar...")

        elif menu == 2:
            conn = db.crear_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM destinos")
            destinos = cur.fetchall()

            if destinos:
                print("\nLista de Destinos:")
                for d in destinos:
                    print(f"ID:{d[0]} - Nombre:{d[1]} - Descripción:{d[2]}")
            else:
                print("No se encontraron destinos.")

            cur.close()
            db.cerrar_conexion(conn)
            input("Presione Enter para continuar...")
        elif menu == 3:
            destino_id = input("Ingrese el ID del destino a modificar: ")
            conn = db.crear_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM destinos WHERE destino_id = %s", (destino_id,))
            destino = cur.fetchone()

            if not destino:
                print(f"No se encontró un destino con ID {destino_id}.")
                cur.close()
                db.cerrar_conexion(conn)
                input("Presione Enter para continuar...")
                continue
            else:
                print(
                    f"Destino encontrado: ID:{destino[0]} - Nombre:{destino[1]} - Descripción:{destino[2]}"
                )
                ciudad1 = (
                    input("Nueva Ciudad (dejar en blanco para no modificar): ")
                    or destino[1]
                )
                descripcion1 = (
                    input("Nueva Descripción (dejar en blanco para no modificar): ")
                    or destino[2]
                )
                precio_noche1 = (
                    input("Nuevo Precio Noche (dejar en blanco para no modificar): ")
                    or destino[3]
                )
                noches1 = (
                    input(
                        "Nueva Cantidad de Noches (dejar en blanco para no modificar): "
                    )
                    or destino[4]
                )

                sqlModificarDestino = "UPDATE destinos SET ciudad = %s, descripcion = %s, precio_noche = %s, noches = %s WHERE destino_id = %s"
                cur.execute(
                    sqlModificarDestino,
                    (ciudad1, descripcion1, precio_noche1, noches1, destino_id),
                )
                conn.commit()
                print(f"Destino {destino_id} modificado con éxito.")
        elif menu == 4:
            print("Saliendo del menú de gestión de destinos...")
            db.cerrar_conexion(db.crear_conexion())
            break
        elif menu == 5:
            print("Volviendo al menú principal...")
            db.cerrar_conexion(db.crear_conexion())
            break
