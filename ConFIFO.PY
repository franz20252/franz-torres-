# Crear una cola vacía
cola_nombres = []

# Ingresar 20 nombres
for i in range(1, 21):
    nombre = input(f"Ingrese el nombre #{i}: ")
    cola_nombres.append(nombre)  # Encolar (agregar al final)

# Mostrar cola antes de extraer
print("\nCola antes de extraer (FIFO):")
print(cola_nombres)

# Extraer un solo nombre usando FIFO
if cola_nombres:
    nombre_extraido = cola_nombres.pop(0)  # Desencolar (quitar el primero)
    print(f"\nNombre extraído (FIFO): {nombre_extraido}")
else:
    print("La cola está vacía.")

# Mostrar cola después de extraer
print("\nCola después de extraer:")
print(cola_nombres)