def mayor_estricto(a, b, c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
    return None

def programa_principal():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))

    resultado = mayor_estricto(a, b, c)

    if resultado is not None:
        print(f"El mayor estricto es: {resultado}")
    else:
        print("No existe un mayor estricto.")

programa_principal()