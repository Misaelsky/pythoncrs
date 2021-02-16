# Obtener numeros

arreglo = [0, 1, 2, 3, 4, 5]

for i in range(0, -100, -1):
    

    residuo = i % 2

    if (i<0 and -100<i and residuo>0):
        print(i)
for i in range(0, 100, 2):
    

    residuo = i % 2

    if (0<i and i<100 and residuo==0):
        print(i)
    else:
        print("NO VALIDO")
        



