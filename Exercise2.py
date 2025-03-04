import numpy as np

# Definir tipo de dato estructurado
dtype = [
    ('codigo', 'int32'),
    ('nombre', 'U20'),
    ('carrera', 'int32'),
    ('promedio', 'float32'),
    ('ingreso', 'int32')
]

# Generar datos aleatorios para los estudiantes
np.random.seed(42)
estudiantes = np.zeros(6500, dtype=dtype)
estudiantes['codigo'] = np.random.randint(2_000_000, 3_000_000, 6500)
estudiantes['nombre'] = [f"Estudiante_{i}" for i in range(6500)]
estudiantes['carrera'] = np.random.randint(10, 73, 6500)
estudiantes['promedio'] = np.round(np.random.uniform(0.0, 5.0, 6500), 1)
estudiantes['ingreso'] = np.random.randint(1944, 2024, 6500)
11
# Filtrar por carrera X, promedio >=4.0
x = int(input("Código carrera a listar (10-72): "))
filtro = (estudiantes['carrera'] == x) & (estudiantes['promedio'] >= 4.0)
seleccion = estudiantes[filtro]
print("\nEstudiantes carrera", x, "con promedio >=4.0:")
print(np.column_stack((seleccion['codigo'], seleccion['nombre'])))
print("Total:", len(seleccion))

# Filtrar ingresados antes de 1990 y condicionales 
filtro = (estudiantes['ingreso'] < 1990) & (estudiantes['promedio'] >= 2.7) & (estudiantes['promedio'] <= 3.2)
seleccion = estudiantes[filtro]
print("\nEstudiantes pre-1990 condicionales:")
print(np.column_stack((seleccion['codigo'], seleccion['nombre'])))
print("Total:", len(seleccion))