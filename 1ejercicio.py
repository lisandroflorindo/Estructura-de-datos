def registrar_alumno():
    print("------ Registro de Inscripción de Alumnos ------")
    
    nombre = input("Ingrese el nombre del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
    
    posee_titulo_secundario = True
    
    monto_matricula = float(input("Ingrese el monto de la matrícula: "))

    cuota = monto_matricula + 1000
    
    arancel = 12000 
    costo_mensual = arancel / 4
    
    print(f"El costo mensual de la materia 'Python I' es: ${costo_mensual:.2f}")
    
    descuento = 0.15
    cuota_con_descuento = cuota * (1 - descuento)
    
    print("\n------ Datos de Inscripción ------")
    print(f"Nombre del alumno: {nombre}")
    print(f"Edad del alumno: {edad}")
    print(f"Fecha de nacimiento del alumno: {fecha_nacimiento}")
    print(f"Posee título secundario: {'Sí' if posee_titulo_secundario else 'No'}")
    print(f"Monto de la matrícula: ${monto_matricula:.2f}")
    print(f"Cuota total (matrícula + $1000): ${cuota:.2f}")
    print(f"Cuota con descuento por pago en efectivo (15%): ${cuota_con_descuento:.2f}")
    print(f"Costo mensual de 'Python I': ${costo_mensual:.2f}")

registrar_alumno()