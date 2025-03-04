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

# ============================================================
# Funciones para Generación de Arrays y Matrices
# ============================================================


# Crear arreglo de ceros
zeros = np.zeros(5)  # 5 elementos con valor 0.0
print("np.zeros:\n", zeros) # Salida: [0. 0. 0. 0. 0.]

# Crear arreglo de unos
ones = np.ones((2, 3))  # Matriz 2x3 con 1.0
print("np.ones:\n", ones)  # [[1. 1. 1.], [1. 1. 1.]]

empty = np.empty((2, 3))  # Valores no inicializados (pueden ser cualquier cosa)
print("np.empty:\n", empty)

print("np.empty:\n", empty)
# Crear matriz identidad
identity = np.eye(3)  # Matriz 3x3 con 1s en diagonal
print("np.eye (Matriz identidad 3x3):\n", identity)  # [[1. 0. 0.], [0. 1. 0.], [0. 0. 1.]]

# Crear arreglo con rango (start, end, step) similar a range() pero devuelve un array
rango = np.arange(2, 10, 2)  # [2, 4, 6, 8]
print("rango:", rango)

# Crear arreglo con n números equidistantes en un intervalo
linspace = np.linspace(0, 1, 5)  # 5 valores entre 0 y 1
print("np.linspace (0, 1, 5):", linspace)  # [0.0, 0.25, 0.5, 0.75, 1.0]

# Crear arreglo con números aleatorios (0-1)
random = np.random.rand(2, 2)  # Matriz 2x2
print("np.random.rand (2x2):\n", random)  # Ej: [[0.48, 0.92], [0.73, 0.15]]

# ============================================================
# Funciones para Operaciones Aritméticas Elementales
# ============================================================

# Suma, resta, multiplicación y división elemento a elemento
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("v1:", v1)
print("v2:", v2)

# Suma: np.add() o el operador +
suma = np.add(v1, v2)  
print("Suma (np.add):", suma)  # [5 7 9]
sumar = v1 + v2 
print("sumar:", sumar) # [5, 7, 9]


# Resta: np.subtract() o el operador -
resta = np.subtract(v2, v1)
print("Resta (np.subtract):", resta)  # [3 3 3]
restar = v2 - v1 
print("Restar:", restar)  # [3 3 3]

# Multiplicación elemento a elemento: np.multiply() o el operador *
multiplicacion = np.multiply(v1, v2)
print("Multiplicación (np.multiply):", multiplicacion)  # [4 10 18]
producto = v1 * v2  # [4, 10, 18]
print("producto:", producto)

# División elemento a elemento: np.divide() o el operador /
division = np.divide(v2, v1)
print("División (np.divide):", division)  # [4. 2.5 2.]


raiz = np.sqrt(v1)  # Raíz cuadrada de cada elemento
print("sqrt:", raiz)  # [1.0, 1.414, 1.732]

# ============================================================
# Funciones Estadísticas Básicas
# ============================================================

# Creamos una matriz de ejemplo
mat = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatriz mat:\n", mat)

# Suma total de elementos: np.sum()
suma_total = np.sum(mat)
print("Suma total (np.sum):", suma_total)  # 21

# Suma por eje (0=columnas, 1=filas)
sum_cols = np.sum(mat, axis=0)  # [4, 6]
sum_filas = np.sum(mat, axis=1)  # [3, 7]
print("sum axis=0:", sum_cols, "sum axis=1:", sum_filas)

# Media: np.mean()
media = np.mean(mat)
print("Media (np.mean):", media)  # 3.5

# Desviación estándar: np.std()
desviacion = np.std(mat)
print("Desviación estándar (np.std):", desviacion)

# Valor mínimo y máximo: np.min() y np.max()
min_val = np.min(mat)
max_val = np.max(mat)
print("Mínimo (np.min):", min_val, ", Máximo (np.max):", max_val)

# ============================================================
# Funciones para Manipulación de Formas y Estructuras
# ============================================================

# Reshape: cambia la forma de un array sin cambiar sus datos
arr = np.arange(12)  # Crea un array de 0 a 11
print("\nArray original:", arr)
arr_reshaped = arr.reshape(3, 4)  # 3 filas, 4 columnas
print("Reshape (3x4):\n", arr_reshaped)

# Transposición: intercambia filas por columnas
transpuesta = np.transpose(arr_reshaped)
print("Transpuesta:\n", transpuesta)

a = np.arange(6)
# Concatenar arreglos
d = np.concatenate([a, a])  # Une dos arreglos
print("concatenate:", d)  # [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]


# Concatenación: une arrays a lo largo de un eje
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
concatenado = np.concatenate((a1, a2), axis=0)  # Concatenar verticalmente
print("Concatenado vertical (axis=0):\n", concatenado)

# También se pueden usar: np.vstack() y np.hstack()
vstacked = np.vstack((a1, a2))  # Apila verticalmente
hstacked = np.hstack((a1, a2))  # Apila horizontalmente
print("vstack:\n", vstacked)
print("hstack:\n", hstacked)


# Dividir arreglos
partes = np.split(a, 3)  # Divide en 3 partes iguales
print("split:", partes)  # [array([0,1]), array([2,3]), array([4,5])]

# ============================================================
# Funciones de Ordenamiento y Selección
# ============================================================

# Ordenar: np.sort() devuelve una copia ordenada del array
unsorted = np.array([3, 1, 2])
sorted_arr = np.sort(unsorted)
print("\nArray sin ordenar:", unsorted)
print("Array ordenado (np.sort):", sorted_arr)

# Indices para ordenar: np.argsort() devuelve los índices que ordenarían el array
indices_orden = np.argsort(unsorted)
print("Indices de ordenamiento (np.argsort):", indices_orden)

# Función única: np.unique() devuelve los valores únicos del array
repetidos = np.array([1, 2, 2, 3, 3, 3])
unique_vals = np.unique(repetidos)
print("Valores únicos (np.unique):", unique_vals)

# ============================================================
# Funciones de Álgebra Lineal
# ============================================================

# Producto punto (dot product) de dos vectores
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product = np.dot(vec1, vec2)
print("\nProducto punto (np.dot):", dot_product)  # 1*4 + 2*5 + 3*6 = 32

# Multiplicación de matrices: np.matmul() o el operador @ (desde Python 3.5+)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
mat_mult = np.matmul(m1, m2)
print("Multiplicación de matrices (np.matmul):\n", mat_mult)
# Alternativamente, se puede usar: m1 @ m2

# Transposición ya vista, pero también es útil en álgebra lineal
print("Transpuesta de m1:\n", m1.T)

# Determinante: np.linalg.det()
determinante = np.linalg.det(m1)
print("Determinante de m1 (np.linalg.det):", determinante)

# Inversa de una matriz: np.linalg.inv()
if np.linalg.det(m1) != 0:
    inversa = np.linalg.inv(m1)
    print("Inversa de m1 (np.linalg.inv):\n", inversa)
else:
    print("La matriz m1 no es invertible.")

# Autovalores y autovectores
autoval, autovec = np.linalg.eig(m1)
print("autovalores:", autoval)  # Ej: [-0.372, 5.372]
print("autovectores:\n", autovec)