def listado_aulas():
    print("Día\tAula")
    for dia in range(1, 7):  
        aula = "A-315" if dia % 2 != 0 else "A-300"
        print(f"{dia}\t{aula}")

listado_aulas()

def cargar_edades():
    errores = 0
    while True:
        try:
            edad = int(input("Ingrese una edad válida (mayor de 18) o -1 para salir: "))
            if edad == -1:
                break
            elif edad < 18:
                errores += 1
                print("Error: La edad debe ser mayor de 18.")
            else:
                print(f"Edad válida ingresada: {edad}")
        except ValueError:
            print("Error: Ingrese un número válido.")
            errores += 1

    print(f"Cantidad de cargas erróneas: {errores}")

cargar_edades()

def promedio_notas():
    total_notas = 0
    for i in range(1, 6): 
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i}: "))
                if 0 <= nota <= 10:
                    total_notas += nota
                    break
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    
    promedio = total_notas / 5
    print(f"El promedio de notas es: {promedio:.2f}")

promedio_notas()

def costo_comedor():
    cuota_diaria = 1250
    print("Día\tCosto Total")
    for dia in range(1, 7):
        costo_total = dia * cuota_diaria
        print(f"{dia}\t${costo_total}")

costo_comedor()