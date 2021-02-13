# Calcular nivel del agua

nivel = float(input("Que nivel de agua tiene la cisterna(en metros)?:"))

if (nivel> 6):
    print("Desbordamiento de agua en cisterna")
elif (nivel == 6):
    print("Apagar bomba")
elif (4<nivel<6):
    print("Desacelerar bomba")
elif (2<nivel<4):
    print("Bomba trabajando")
elif (0<nivel<2):
    print("Acelerar bomba")
elif (nivel== 0):
    print("Encender bomba")
elif (nivel < 0):
    print("FUGA")

