from models.cliente import Cliente
from utils.helpers import pedir_opcion, pedir_entero, pedir_texto, pedir_numero, pedir_fecha
from services.cita_service import calcular_total, ordenar_clientes, ingresos_totales, contar_extracciones, contar_urgentes

clientes = []

def pedir_cliente():
    cedula = pedir_numero("Cédula: ")
    nombre = pedir_texto("Nombre: ")
    telefono = pedir_numero("Teléfono: ")

    tipo_cliente = pedir_opcion(
        "Tipo cliente (particular/eps/prepagada): ",
        ["particular", "eps", "prepagada"]
    )

    tipo_atencion = pedir_opcion(
        "Tipo atención (limpieza/calzas/extraccion/diagnostico): ",
        ["limpieza", "calzas", "extraccion", "diagnostico"]
    )

    if tipo_atencion in ["limpieza", "diagnostico"]:
        print("Para este tipo de atención la cantidad es 1 automáticamente.")
        cantidad = 1
    else:
        cantidad = pedir_entero("Cantidad: ")

    prioridad = pedir_opcion(
        "Prioridad (normal/urgente): ",
        ["normal", "urgente"]
    )

    fecha = pedir_fecha("Fecha (dd/mm/aaaa): ")

    return Cliente(
        cedula, nombre, telefono,
        tipo_cliente, tipo_atencion,
        cantidad, prioridad, fecha
    )

def mostrar_menu():
    print("""
        --- MENÚ ---
        1. Registrar cliente
        2. Ver estadísticas
        3. Buscar cliente
        4. Salir
        """)

def registrar_cliente():
    cliente = pedir_cliente()
    calcular_total(cliente)
    clientes.append(cliente)
    print("Cliente registrado correctamente.\n")

def mostrar_estadisticas():
    print("\n--- RESULTADOS ---")
    print("Total clientes:", len(clientes))
    print("Ingresos:", ingresos_totales(clientes))
    print("Extracciones:", contar_extracciones(clientes))
    print("Clientes urgentes:", contar_urgentes(clientes))

    ordenados = ordenar_clientes(clientes)

    print("\n--- CLIENTES ORDENADOS ---")
    for c in ordenados:
        print(f"{c.nombre} | {c.tipo_atencion} | ${c.total}")


def buscar_cliente():
    cedula = input("\nBuscar cédula: ")

    for c in clientes:
        if c.cedula == cedula:
            print(f"""
--- Cliente encontrado ---
Cédula: {c.cedula}
Nombre: {c.nombre}
Teléfono: {c.telefono}
Tipo cliente: {c.tipo_cliente}
Tipo atención: {c.tipo_atencion}
Cantidad: {c.cantidad}
Prioridad: {c.prioridad}
Fecha: {c.fecha}
Total: ${c.total}
""")
            return  

    print("Cliente no encontrado")

def ejecutar_app():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            mostrar_estadisticas()

        elif opcion == "3":
            buscar_cliente()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida\n")