import datetime

def es_fecha_valida(dia, mes, anio):
    try:
        fecha = datetime.date(anio, mes, dia)
        return True
    except ValueError:
        return False
    
def probar_fecha():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    
    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

probar_fecha() 