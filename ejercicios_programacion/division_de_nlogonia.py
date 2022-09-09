#Ejercicio de coordenadas

# NE NO SO SE divisa

while True:
    iteraciones = input()

    if iteraciones != '0':
        n = input()
        m = input()

        for i in range(iteraciones):
            a = input()
            b = input()

            if(a>n and b>m):
                print("NE")
            elif(a<n and b>m):
                print("NO")
            elif(a<n and b<m):
                print("SO")
            elif(a>n and b<m):
                print("SE")
            else:
                print("divisa")
    else:
        break

    class persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

adolfo = persona("Adolfo", 20)            