# Determinar si es par o impar

numero = input("Inserta un numero entero:")

calculo = int(numero)

residuo = int(calculo) % 2


if (residuo>0):
    print ("impar")
else:
    print("par") 
