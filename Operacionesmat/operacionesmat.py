# Realizar sum
print("Escribe un numero:")
num1 = input()
num2 = input("Escribe otro numero:")

# Operacion de suma
suma = float(num1) + float(num2)
resta = float(num1) - float(num2)
multiplicacion = float(num1) * float(num2)
division = float(num1) / float(num2)

potencia1 = float(num1) ** float(num2)
potencia2 = pow(float(num1), float(num2))
raiz_cuad = pow(float(num1), float(1/2))
raiz_cub = pow(float(num1), float(1/3))


# Impresiones
print(suma)
print(type(suma))
print(resta)
print(multiplicacion)
print(division)
print(potencia1)
print(potencia2)
print(raiz_cuad)
print(raiz_cub)