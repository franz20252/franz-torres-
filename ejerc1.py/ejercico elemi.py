# Crear la pila con 15 elementos
pila = [i for i in range(1, 16)]
print("Pila original:", pila)

# Eliminar el 3er y 7mo elemento desde el inicio (índices 2 y 6)
eliminados = []
for i in sorted([6, 2], reverse=True):  # Eliminar primero el índice mayor para no desordenar
    eliminados.append(pila.pop(i))

print("Elementos eliminados:", eliminados)
print("Pila final:", pila)
