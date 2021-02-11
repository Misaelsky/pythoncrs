# deberas ingresar tus tres calificaciones para obtener tu promedio
cal1 = int(input("Calificacion 1 Parcial:"))
cal2 = int(input("Calificacion 2 Parcial:"))
cal3 = int(input("Calificacion 3 Parcial:"))

promedio = (cal1 + cal2 + cal3) / 3

if (promedio>=6):
    print("Aprobado")
else:
    print("Reprobado")

print(promedio)