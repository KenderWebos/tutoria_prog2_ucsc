# https://www.beecrowd.com.br/judge/es/problems/view/1042

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