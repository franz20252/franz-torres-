# Crear la pila usando un bucle for
pila = []
for i in range(1, 16):
    pila.append(i)

# Eliminar el tercer y séptimo número (índices 2 y 6)
pila.pop(6)  # Elimina el séptimo número
pila.pop(2)  # Elimina el tercer número

# Mostrar la pila resultante
print("Pila después de eliminar el tercer y séptimo número:")
for numero in pila:
    print(numero)