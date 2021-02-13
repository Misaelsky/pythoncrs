# Definir una función:
# Tarea a ejecutar (argumentos o parámetros) puede devolver o retornar un valor

def Saludo():
    print("Función en ejecución...")

Saludo()

def Sumar(a, b):
    return a + b

suma = Sumar(10, 12)
print(suma)

def CompararDosNumeros(x, y):
    if x > y:
        print(f"{x} es mayor a {y}")
    elif x < y:
        print(f"{x} es menor a {y}")
    else:
        print(f"{x} es igual a {y}")

CompararDosNumeros(15, 5)