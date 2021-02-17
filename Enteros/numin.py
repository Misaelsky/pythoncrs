# Ciclos de entero
num = int(input("Ingresa un número entero: "))
suma = 0
suma= suma + num
contador = 0



if num>0:
    contador += 1

while num>0:
    try:
        num = int(input("Ingresa un número entero: "))
        if num>0:
            suma = suma + num
            contador = contador + 1
            promedio = suma / contador
            
    except:
        print("Dato inválido")


print(float(promedio))






