
# Programa: Reserva de un asiento en sala de cine
# Descripción: Gestiona la reserva de asientos en una matriz de 3x4 utilizando listas anidadas y bucles anidados en Python.

asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("--- SISTEMA DE RESERVA DE CINE ---")

while True:
    try:
        fila = int(input("Ingrese el número de fila (0 a 2): "))
        columna = int(input("Ingrese el número de columna (0 a 3): "))

        if 0 <= fila <= 2 and 0 <= columna <= 3:
            asientos[fila][columna] = 1
            print(f"\n¡Éxito! El asiento en la Fila {fila}, Columna {columna} ha sido reservado.\n")
            break
        else:
            print("Error: Índices fuera de rango. Recuerde que la fila es de 0 a 2 y la columna de 0 a 3.\n")
    except ValueError:
        print("Error: Ingrese únicamente números enteros válidos.\n")

print("Estado actual de la sala (0 = Libre, 1 = Reservado):")
print("-" * 30)

for i in range(len(asientos)):
    # Recorrido de las columnas
    for j in range(len(asientos[i])):
        print(asientos[i][j], end="  ")
    print()

print("-" * 30)