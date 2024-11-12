import random as rd
numeros_100 = [rd.randint(1, 1000) for _ in range(100)]
numeros_500 = [rd.randint(1, 1000) for _ in range(500)]
numeros_1000 = [rd.randint(1, 1000) for _ in range(1000)]
numeros_5000 = [rd.randint(1, 1000) for _ in range(5000)]
numeros_10000 = [rd.randint(1, 1000) for _ in range(10000)]
numeros_20000 = [rd.randint(1, 1000) for _ in range(20000)]

# Crear contenido con saltos de línea para cada archivo
numeros_str_100 = "\n".join(map(str, numeros_100))
numeros_str_500 = "\n".join(map(str, numeros_500))
numeros_str_1000 = "\n".join(map(str, numeros_1000))
numeros_str_5000 = "\n".join(map(str, numeros_5000))
numeros_str_10000 = "\n".join(map(str, numeros_10000))
numeros_str_20000 = "\n".join(map(str, numeros_20000))

# Guardar los números en archivos de texto
file_path_100 = 'arc1.txt'
file_path_500 = 'arc2.txt'
file_path_1000 = 'arc3.txt'
file_path_5000 = 'arc4.txt'
file_path_10000 = 'arc5.txt'
file_path_20000 = 'arc6.txt'

with open(file_path_100, 'w') as file:
    file.write(numeros_str_100)

with open(file_path_500, 'w') as file:
    file.write(numeros_str_500)

with open(file_path_1000, 'w') as file:
    file.write(numeros_str_1000)

with open(file_path_5000, 'w') as file:
    file.write(numeros_str_5000)

with open(file_path_10000, 'w') as file:
    file.write(numeros_str_10000)

with open(file_path_20000, 'w') as file:
    file.write(numeros_str_20000)