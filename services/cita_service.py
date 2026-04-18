from data.tarifas import TARIFAS

def calcular_total(cliente):
    valor_cita = TARIFAS[cliente.tipo_cliente]["cita"]
    valor_atencion = TARIFAS[cliente.tipo_cliente]["atencion"][cliente.tipo_atencion]

    if cliente.tipo_atencion in ["Limpieza", "Diagnostico"]:
        cliente.cantidad = 1

    cliente.total = valor_cita + (valor_atencion * cliente.cantidad)


def contar_extracciones(clientes):
    return sum(1 for c in clientes if c.tipo_atencion.lower() == "extraccion")


def ingresos_totales(clientes):
    return sum(c.total for c in clientes)


def ordenar_clientes(clientes):
    return sorted(clientes, key=lambda c: c.total, reverse=True)

def contar_urgentes(clientes):
    return sum(1 for c in clientes if c.prioridad == "urgente")

