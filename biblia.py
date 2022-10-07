import sys
import os
import math

### 👉 REEMPLAZAR PARTES DE UN ARRAY 👀 ###

# s = "Este A es un A texto que A A muestra A A A como reemplazar A partes de un A string"
# s = s.replace("A ","")
# print(s)

# s = s.replace("un string","una cadena de caracteres")
# print(s)

### 👉 ALMACENAR UNICAMENTE LAS PALABRAS QUE NO SE REPITEN 👀 ###

# palabras = ["Huevos", "Queso", "Lechuga", "Tomate", "Huevos", "Lechuga", "Huevos"]

# palabras = set( palabras )

# print( f"la comida que tenemos son: {palabras}" )

# # QUE PASA SI TENGO HUEVOS, huevos y Huevos ?

### 👉 REVOLVER UN ARRAY 👀 ###

# import random
# persons = ["david", "mari", "adolf", "kindirmin", "ricar2"]
# random.shuffle(persons)
# print( persons )

### 👉 ESCOGER UN ELEMENTO DE UN ARRAY RANDOM 👀 ###

# import random
# persons = ["david", "mari", "adolf", "kindirmin", "ricar2"]
# print(random.choice(persons))

### 👉 FUNCIONES ANONIMAS Y MAPEO 👀 ###

# def sayMapeado(palabra):
#     return palabra + " y ahora esta mapeado"

# nombres = ["KenderWebos", "Tugo15", "Celipito"]
# numeros = [1, 2, 3]

# a = map(sayMapeado, nombres)

# print( list(a) )

# print( list(map(lambda x:x+x, nombres)) )

# numbers = [1, 2, 3]

# print( list( map( lambda x: x+x, numbers ) ) )
# input()

### 👉 MAPEAR PARA CONTAR LOS ASCII DE UNA PALABRA 👀 ###

# palabra = "kenderwebos"
# print( sum(map(ord, palabra)) )

# palabra = "cesar"
# a = []
# for i in range (len(palabra)):
#     a.append(ord(palabra[i]))
# a = sum(a)
# print(a)

# numbers = [1,2,3]
# # print( list( map(lambda x:x+x, (int(input())).split ) ) )
# print( list( map(lambda x:x+x, numbers) ) )
# input()

### 👉 *args 👀 ###

# def saludar(*args):
#     for x in args:
#         print(f"Hola soy {x}, gusto en conocerte.")

# saludar( "Pedro", "Juan", "Diego" )

### 👉 FINAL DEL DOCUMENTO 👀 ###

input()