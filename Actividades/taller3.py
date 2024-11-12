import random as rd #libreria random

def partition(A, p, r):
    x = A[r]  #2 Elige el pivote como el último elemento (basandose en el algoritmo del libro)
    print("pivote escogido: ",x)

    i = p - 1  # i se inicializa como el índice anterior al primero

    for j in range(p, r):
        print("iteración #",j+1,", elemento ",A[j])
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # Intercambia A[i] con A
            print(A[i], "es MENOR que el pivote se pasa a la IZQUIERDA en "
                        "la posicion: ", i, "       VECTOR: ", A)
        else:
            print(A[j],"es MAYOR que el pivote se mantiene a la DERECHA       VECTOR: ",A)
    finPivote=i+1
    A[finPivote], A[r] = A[r], A[i + 1]  # Coloca el pivote en su posición final

    return finPivote  # Retorna la posición del pivote

def comprobarVector(A, indPiv):
    bandera = True
    for i in range((indPiv+1),len(A)):

       if A[i]<A[indPiv]:
           bandera = False


    for i in range((indPiv-1),0,-1):
       if A[i]>A[indPiv]:
           bandera = False

    if bandera:
        print("El pivote cumple la condicion")
    else:
        print("El pivote no cumple la condicion")

B = rd.sample(range(100, 200), 5)
print(B)
pivot_index = partition(B, 0, len(B) - 1)

print("Arreglo después de la partición:", B)
print("Índice del pivote:", pivot_index)
comprobarVector(B,pivot_index)