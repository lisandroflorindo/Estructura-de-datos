def obtener_datos_alumno():
    nota1 = float(input("Ingrese la nota del primer examen: "))
    nota2 = float(input("Ingrese la nota del segundo examen: "))
    
    return nota1, nota2

def calcular_promedio(nota1, nota2):
    return (nota1 + nota2) / 2

def determinar_aprobacion(nota2):
    if nota2 >= 7:
        return "Aprobó el segundo examen"
    else:
        return "Desaprobó el segundo examen"

def comparar_desempeno(nota1, nota2):
    if nota2 > nota1:
        return "Mejoró su desempeño"
    elif nota2 < nota1:
        return "Empeoró su desempeño"
    else:
        return "Mantuvo la nota"

def determinar_estado_final(promedio):
    if promedio >= 7:
        return "Promocionó la materia"
    elif promedio >= 4:
        return "Debe rendir final"
    else:
        return "Debe recursar"

def main():
    nota1, nota2 = obtener_datos_alumno()
    
    promedio = calcular_promedio(nota1, nota2)
    
    resultado_examen = determinar_aprobacion(nota2)
    
    resultado_desempeno = comparar_desempeno(nota1, nota2)
    
    estado_final = determinar_estado_final(promedio)
    
    print("\nResultados del alumno:")
    print(f"Promedio de notas: {promedio:.2f}")
    print(resultado_examen)
    print(resultado_desempeno)
    print(estado_final)

if __name__ == "__main__":
    main()