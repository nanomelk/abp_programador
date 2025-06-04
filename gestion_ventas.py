import conexion_base_datos as db
from datetime import datetime, date, timedelta


def menu_ventas():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Botón de Compra")
        print("2. Botón de Reversión")
        print("3. Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            boton_compra()

        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def boton_compra():
    cuit = input("Ingrese su CUIT: ")
    conexion = db.crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
    cliente = cursor.fetchone()
    if not cliente:
        print(f"No se encontró un cliente con CUIT/CUIL {cuit}.")
        input("Presione Enter para continuar...")
        return
    else:
        print(f"Cliente encontrado: {cliente[1]} - {cliente[0]} - {cliente[2]}")

    destino_id = input("Ingrese el destino_id del viaje: ")
    cursor.execute(
        "SELECT * FROM destinos WHERE destino_id = %s",
        (destino_id,),
    )
    destino = cursor.fetchone()

    if not destino:
        print("No se encontró ese destino.")
        input("Presione Enter para continuar...")
        return

    precio_final = destino[3] * destino[4]
    print(f"Destino seleccionado: {destino[1]}, Precio Final: {precio_final}")

    # Ingreso y validación de fecha de salida
    try:
        dia = int(input("Ingrese el día de salida: "))
        mes = int(input("Ingrese el mes de salida: "))
        anio = int(input("Ingrese el año de salida: "))
        fecha_salida = date(anio, mes, dia)
    except ValueError:
        print("Fecha inválida. Intente de nuevo.")
        return

    fecha_venta = datetime.now()

    # Insertamos en la tabla ventas (estado_id lo dejamos fijo por ejemplo en 1)
    cursor.execute(
        """
        INSERT INTO ventas (cuit, estado_id, destino_id, fecha_venta, fecha_salida)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (cuit, 1, destino_id, fecha_venta, fecha_salida),
    )

    conexion.commit()
    cursor.close()
    db.cerrar_conexion(conexion)

    print("Compra registrada con éxito.")
    input("Presione Enter para continuar...")


def boton_arrepentimiento():
    print("\n--- Botón de Arrepentimiento ---")
    print("Condiciones:")
    print("1. Dentro de los 60 días hábiles desde la compra.")
    print("2. No aplica si el pasaje fue utilizado o faltan menos de 72h.")

    numero_reserva = input("Ingrese el número de reserva: ")

    conexion = db.crear_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT fecha_venta, fecha_salida, estado_id FROM ventas WHERE ventas_id = %s",
        (numero_reserva,),
    )
    resultado = cursor.fetchone()

    if not resultado:
        print(f"No se encontró una reserva con número {numero_reserva}.")
        return

    fecha_venta, fecha_salida, estado_id = resultado
    ahora = datetime.now()

    diferencia = ahora - fecha_venta

    # CONDICIÓN COMBINADA: si pasó más de 60 días O faltan menos de 72 hs
    if diferencia > timedelta(days=60) or (fecha_salida - ahora.date()) < timedelta(
        days=3
    ):
        print(
            "No se puede cancelar: pasó más de 60 días desde la compra o faltan menos de 72 horas para la salida."
        )
        return

    print(f"Reversión solicitada para la reserva {numero_reserva}.")
    print("¿Cancelar la compra?")
    print("1. Sí\n2. No")
    opcion = int(input("Elija la opción: "))

    if opcion == 1:
        cursor.execute(
            "UPDATE ventas SET estado_id = %s WHERE ventas_id = %s", (2, numero_reserva)
        )
        conexion.commit()
        print(f"La reserva {numero_reserva} ha sido cancelada.")
    else:
        print("Operación cancelada.")

    cursor.close()
    db.cerrar_conexion(conexion)
    input("Presione Enter para volver al menú principal...")
