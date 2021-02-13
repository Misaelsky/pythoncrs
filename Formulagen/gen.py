# Calcular formula general
va = float(input("Inserta valor de a:"))
vb = float(input("Inserta valor de b:"))
vc = float(input("Inserta valor de c:"))

cfguno= (-vb + pow(pow(vb,2) -4*(va*vc), 1/2)) / 2*va
cfgdos= (-vb - pow(pow(vb,2) -4*(va*vc), 1/2)) / 2*va

print(str(cfguno) + " x1 y " + str(cfgdos) + " x2")