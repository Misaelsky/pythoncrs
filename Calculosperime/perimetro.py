# Calucular area y perimetro

radio = input("Inserta el radio de tu circulo:")

radioc = float(radio)

import math

valorpi = math.pi

area = valorpi * pow(radioc,2)

perimetro = 2 * valorpi * radioc

print("El area del circulo es:" + str(area) + "cm^2")
print("El perimetro del circulo es:" + str(perimetro) + "cm")
