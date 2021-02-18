
def Print(a, b, c, d, e, f, g, h, i, j):
    return a, b, c, d, e, f, g, h, i, j

arreglo = Print(10, 8, 3, 7, 14, 9, 13, 4, 75, 5)
print(arreglo)

def Print2(Lista):
    for item in Lista:
        if item > 5:
            print(item)

Lista = [0,1,2,3,4,5,6,7,8,9]

Print2(Lista)


