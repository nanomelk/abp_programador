def boton_arrepentimiento():
    print("\n--- Botón de Arrepentimiento ---")
    print("Condiciones:")
    print("1. Dentro de los 60 días hábiles desde la compra.")
    print("2. No aplica si el pasaje fue utilizado o faltan menos de 72h.")

    numero_reserva = input("Ingrese el número de reserva: ")
    print(f"Reversión solicitada para la reserva {numero_reserva}.")
    print("¿Cancelar la compra?")
    print("1. Sí\n2. No")
    opcion = int(input("Elija la opción: "))

    if opcion == 1:
        print(f"La reserva {numero_reserva} ha sido cancelada.")
    else:
        print("Operación cancelada.")

    input("Presione Enter para volver al menú principal...")
