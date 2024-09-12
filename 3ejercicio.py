def asignar_aula(dia):
    """
    Determina el aula asignada en función del día de la semana.
    """
    if dia < 1 or dia > 6:
        return "Día inválido. Por favor, ingrese un número entre 1 y 6."
    
    if dia % 2 == 0:
        return "Los alumnos cursan en el aula A-300."
    else:
        return "Los alumnos cursan en el aula A-315."

def calcular_descuento(turno, num_materias, cuota_base):
    """
    Calcula el descuento en la cuota según el turno y la cantidad de materias.
    """
    if turno.lower() == "tarde" and num_materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05
    
    cuota_con_descuento = cuota_base * (1 - descuento)
    return cuota_con_descuento

def costo_estacionamiento(vehiculo, dias):
    """
    Calcula el costo del estacionamiento según el tipo de vehículo.
    """
    if vehiculo.lower() in ["auto", "moto"]:
        costo_diario = 300
    elif vehiculo.lower() == "bicicleta":
        costo_diario = 50
    else:
        return "Tipo de vehículo inválido."
    
    costo_total = costo_diario * dias
    return costo_total

# Ejemplo de uso:

# a. Asignación de aula
dia = int(input("Ingrese el número de día (1 a 6): "))
print(asignar_aula(dia))

# b. Cálculo de descuento en la cuota
turno = input("Ingrese el turno (Mañana/Tarde): ")
num_materias = int(input("Ingrese el número de materias en las que se inscribe: "))
cuota_base = float(input("Ingrese el valor de la cuota base: "))
cuota_con_descuento = calcular_descuento(turno, num_materias, cuota_base)
print(f"El valor de la cuota con descuento es: ${cuota_con_descuento:.2f}")

# c. Cálculo del costo de estacionamiento
vehiculo = input("Ingrese el tipo de vehículo (auto/moto/bicicleta): ")
dias = int(input("Ingrese el número de días que utilizará el estacionamiento: "))
costo = costo_estacionamiento(vehiculo, dias)
print(f"El costo total de estacionamiento es: ${costo}")