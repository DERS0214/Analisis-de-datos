import time

def stoogesort(arr, l, h):
    if l >= h:
        return

    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)

        stoogesort(arr, l, (h - t))
        stoogesort(arr, l + t, (h))
        stoogesort(arr, l, (h - t))
#GeeksforGeeks. (n.d.). Python program for Stooge Sort. GeeksforGeeks.
#https://www.geeksforgeeks.org/python-program-for-stooge-sort/

def leerArchivo(filename):
    with open(filename, 'r') as file:
        data = file.read().split()
        return list(map(int, data))

filename = "arc3.txt"

# Leer los datos desde el archivo
arr = leerArchivo(filename)

# Medir el tiempo de ejecución del algoritmo
start_time = time.time()  # Hora de inicio
n = len(arr)
stoogesort(arr, 0, n - 1)  # Llamada al algoritmo Stoogesort
end_time = time.time()  # Hora de fin

# Mostrar el arreglo ordenado
print("Arreglo ordenado:")
for num in arr:
    print(num, end=' ')

# Mostrar el tiempo de ejecución
print(f"\nTiempo de ejecución: {end_time - start_time:.6f} segundos")
print("David Enrique Ramirez Scamaronez")
print("Paralelo 2")
print("12-11-2024")