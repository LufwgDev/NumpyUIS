#Según la página principal de Numpy, https://numpy.org/doc/stable/:
#NumPy es el paquete fundamental para la computación científica en Python.
#Es una biblioteca de Python que proporciona un objeto de arreglo multidimensional,
#varios objetos derivados (como matrices y arreglos enmascarados)
#y una variedad de rutinas para operaciones rápidas en matrices,
#incluidas operaciones matemáticas, lógicas, manipulación de formas, ordenamiento,
#selección, E/S, transformadas discretas de Fourier, álgebra lineal básica,
#operaciones estadísticas básicas, simulación aleatoria y mucho más.


#Cómo importar NumPy
#Después de instalar NumPy, se puede importar al código Python de la siguiente manera:
import numpy as np

#Fundamentos de un arreglo
#Declarar/inicializar
a = np.array([1, 2, 3, 4, 5, 6])
print("a",a)

#acceder a un elemrnto del arreglo por medio de su índice (como con las listas)
print("a",a[0])

#Arreglos también son "mutables"
a[0]=10

print("a",a)


#misma notación "slice" que con las listas
print("a",a[:3])

#Una diferencia importante es que la indexación de una lista mediante segmentos (slice)
#copia los elementos en una nueva lista, pero la segmentación de una matriz
#devuelve una "vista": un objeto que hace referencia a los datos de la matriz original.
#La matriz original se puede modificar mediante la "vista".

b = a[3:]
print("b",b)
b[0]=40
print("a",a)

#Se pueden inicializar matrices bidimensionales y de dimensiones superiores a partir de secuencias anidadas de Python:
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("c",c)

#Sintaxis diferente a la de las listas
print("c",c[1,3])

#Atributos de Array (Arreglo) 

#Número de dimensiones
print("ndim",c.ndim)
#Cantidad de elementos en cada eje o dimensión
print("shape",c.shape)

print(len(c.shape)==c.ndim) #True

#Cantidad total de elemtentos en un arreglo
print("size",c.size)

import math
print(c.size==math.prod(c.shape)) #True
