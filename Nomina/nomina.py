# Calcular la nomina de un empleado

dia = float(input("Escriba su sueldo del dia:"))

mes = dia *31

brut = mes * 1.16

ivat = mes * 0.16 * (2 / 3 )

isr = mes * 0.10

sueldo = brut - ivat - isr

print("Tu sueldo mensual es:" + str(sueldo))

