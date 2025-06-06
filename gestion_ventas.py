import conexion_base_datos as db
from datetime import datetime, date


def menu_ventas():
    # funcion menu, se usa while True para que se repita hasta que el usuario decida salir
    while True:
        print("\n--- Menú Principal ---")
        print("1. Botón de Compra")
        print("2. Botón de Reversión")
        print("3. Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            boton_compra()
        elif opcion == 2:
            listar_ventas()

        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def boton_compra():
    # pedimos el CUIT del cliente
    cuit = input("Ingrese su CUIT: ")
    # abrimos la conexión a la base de datos
    conexion = db.crear_conexion()
    cursor = conexion.cursor()
    # Verificamos si existe el cliente
    cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
    # obtenemos datos del cliente y lo cargamos en la variable cliente
    # si no existe el cliente, mostramos un mensaje y volvemos al menú principal
    cliente = cursor.fetchone()
    if not cliente:
        print(f"No se encontró un cliente con CUIT/CUIL {cuit}.")
        input("Presione Enter para continuar...")
        return
    else:
        print(f"Cliente encontrado: {cliente[1]} - {cliente[0]} - {cliente[2]}")
    # Pedimos el destino_id del viaje, el usuario debe saber su destino_id (futora funcionalidad puede listar los destinos disponibles))
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
    # calcula el precio final del viaje multiplicando el precio por la cantidad de noches
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


def listar_ventas():
    # abrimos la conexión a la base de datos
    conexion = db.crear_conexion()
    cursor = conexion.cursor()
    # Obtenemos todas las ventas
    cursor.execute(
        """
        SELECT v.ventas_id, c.razon_social, d.ciudad, v.fecha_venta, v.fecha_salida, e.tipo_estado, d.precio_noche, d.noches
        FROM ventas v
        JOIN clientes c ON v.cuit = c.cuit
        JOIN destinos d ON v.destino_id = d.destino_id
        JOIN estado e ON v.estado_id = e.estado_id
        ORDER BY v.fecha_venta DESC
    """
    )
    ventas = cursor.fetchall()

    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("\n--- Lista de Ventas ---")
        for venta in ventas:
            print(
                f"Reserva ID: {venta[0]}, Cliente: {venta[1]}, Destino: {venta[2]}, "
                # La variable Costo total es calculada multiplicando el precio por la cantidad de noches - evitando agregrar a la base este campo que puede ser calculado
                f"Fecha de Venta: {venta[3]}, Fecha de Salida: {venta[4]}, Estado: {venta[5]}, Costo Total: {venta[6] * venta[7]}"
            )

    cursor.close()
    db.cerrar_conexion(conexion)
    input("Presione Enter para volver al menú principal...")


def boton_arrepentimiento():
    print("\n--- Botón de Arrepentimiento ---")
    print("Condiciones:")
    print("1. Dentro de los 60 dias (por escala esta en minutos) desde la compra.")
    print("2. No aplica si el pasaje fue utilizado o faltan menos de 72h.")

    # Pedimos el número de reserva
    numero_reserva = input("Ingrese el número de reserva: ")
    # abrimos la conexión a la base de datos
    conexion = db.crear_conexion()
    cursor = conexion.cursor()
    # Verificamos si existe la reserva
    cursor.execute(
        "SELECT fecha_venta, fecha_salida, estado_id FROM ventas WHERE ventas_id = %s",
        (numero_reserva,),
    )
    # Obtenemos datos de la reserva a cancelar y lo cargamos en la variable resultado
    resultado = cursor.fetchone()

    if not resultado:
        print(f"No se encontró una reserva con número {numero_reserva}.")
        return
    # Desempaquetamos los datos de la reserva
    fecha_venta, fecha_salida, estado_id = resultado
    ahora = datetime.now()

    # Convertimos fecha_salida (que es date) a datetime a las 00:00
    fecha_salida_dt = datetime.combine(fecha_salida, datetime.min.time())

    # Cuánto tiempo pasó desde que se compró (en minutos)
    diferencia_minutos = (ahora - fecha_venta).total_seconds() / 60

    # Cuánto falta para que salga el viaje (en horas)
    diferencia_horas_salida = (fecha_salida_dt - ahora).total_seconds() / 3600

    if diferencia_minutos > 60:
        print("No se puede cancelar: pasaron más de 60 minutos desde la compra.")
        return

    if diferencia_horas_salida < 72:
        print("No se puede cancelar: faltan menos de 72 horas para la salida.")
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
