# Calcular la nomina de un empleado

dia = float(input("Escriba su sueldo del dia:"))

mes = dia *30.4

iva = mes *0.16

ivat = iva * (2 / 3 )

isr = mes * 0.10

sueldo = mes - ivat - isr

print("Tu sueldo mensual es:" + str(sueldo))

