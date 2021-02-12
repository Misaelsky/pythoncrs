# Calcular temperatura

temperatura = input("Inserta temperatura:")
temp = float(temperatura)
unidad = str(input("Asigna unidad de la temperatura (ya sea K, F o C):"))
celsius = str("C")
far = str("F")
kelvin  = str("K")

caf = (temp * (9 / 5)) + 32
cak = temp + 273.15
fac = (temp - 32) * (5/9)
fak = ((temp - 32) * (5/9)) + 273.15
kac = temp - 273.15
kaf = ((temp - 273.15) * (9/5)) + 32





if(unidad == celsius):
    print(str(caf) + " F " + str(cak) + " K")
elif(unidad == far):
    print(str(fac) + " C " + str(fak) + " K")
elif(unidad == kelvin):
    print(str(kac) + " C " + str(kaf) + " F")
else:
    print("Inserte unidad valida")


