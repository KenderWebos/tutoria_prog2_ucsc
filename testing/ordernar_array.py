# a = 5 #entero int
# b = "hola" #string

# c = 'a' #cahracter

# d = 5.5 #float

# estaLloviendo = True #boolean

# print("ingrese su nombre: ")
# nombre = input()

# print("ingrese su edad: ")
# edad = input()

# print("Hola mi nombre es " + nombre + "\n y tengo " + edad + " años")
# #print( "Hola mi nombre es" , nombre , "y tengo" , edad , "años" )
# # print( f"Hola mi nombre es {nombre}" )

# def suma(a,b): #esta funcion recibe dos parametros y
#     print( a + b )

# numeroBueno = int("5")

# # print( suma(numeroBueno, numeroBueno) )

# # def saludar():
# #     print("Hola")

# # saludar()

# suma(4,10)

# Lea tres números enteros y ordénelos en orden ascendente. 
# Después, imprima estos valores en orden ascendente, 
# una línea en blanco y luego los valores en la secuencia tal como fueron leídos.

numeros = []
for i in range(3):
    numeros.append( input() )

nuevoArray = numeros.copy()

numeros.sort()

# la funcion id() nos deja ver la direccion de memoria de una variable
# print( id(numeros) )
# print( id(nuevoArray) )

print( numeros )
print( nuevoArray )
