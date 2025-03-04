import numpy as np

# Ejercicio 1: Representante de estudiantes
np.random.seed(0)
votos = np.random.randint(1, 31, 5000)           # 5000 votos para candidatos 1 a 30
cuenta = np.bincount(votos)[1:]                  # Conteo de votos (índice 0 se descarta)
orden = np.argsort(cuenta)[::-1] + 1             # Candidatos ordenados de mayor a menor

print("Listado de candidatos de mayor a menor votos:")
for candidato in orden:
    print("Candidato", candidato, "votos:", cuenta[candidato - 1])


