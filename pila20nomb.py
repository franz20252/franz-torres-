# Crear una pila vacía
pila_nombres = []

# Ingresar 20 nombres
for i in range(1, 21):
    nombre = input(f"Ingrese el nombre #{i}: ")
    pila_nombres.append(nombre)  # Push a la pila

# Mostrar pila antes del cambio
print("\nPila antes de extraer (LIFO):")
print(pila_nombres)

# Extraer un solo nombre usando LIFO
if pila_nombres:
    nombre_extraido = pila_nombres.pop()  # Pop del último ingresado
    print(f"\nNombre extraído (LIFO): {nombre_extraido}")
else:
    print("La pila está vacía.")

# Mostrar pila después del cambio
print("\nPila después de extraer:")
print(pila_nombres)