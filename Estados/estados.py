# Imprimir los arreglos de un diccionario

data = [
            {"ciudad" : "Ciudad de Mexico", "Poblacion" : "8.85 M", "Extension en KM2" : 1.485},
            {"ciudad" : "Estado de Mexico", "Poblacion" :"16.99 M", "Extension en KM2" : 22.500},
            {"ciudad" : "Michoacan", "Poblacion" : "4.749 M", "Extension en KM2" : 58.599},
            {"ciudad" : "Jalisco", "Poblacion" : "8.348 M", "Extension en KM2" : 78.588},
            {"ciudad" : "San Luis Potosi", "Poblacion" : "2.822 M", "Extension en KM2" : 61.137},
            {"ciudad" : "Guanajuato", "Poblacion" : "6.167 M", "Extension en KM2" : 30.607},
        ]



for d in data:
    if d["Extension en KM2"] >= 1:
        print(d)
        print("************************************************************")
        


