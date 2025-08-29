class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.queue = [None] * capacidad
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.capacidad == self.front

    def enqueue(self, elemento):
        if self.isFull():
            print("⚠️ La cola está llena")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacidad
        self.queue[self.rear] = elemento

    def dequeue(self):
        if self.isEmpty():
            print("⚠️ La cola está vacía")
            return None
        elemento = self.queue[self.front]
        if self.front == self.rear:
            # Solo había un elemento
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacidad
        return elemento

    def peek(self):
        if self.isEmpty():
            return "⚠️ La cola está vacía"
        return self.queue[self.front]

    def size(self):
        if self.isEmpty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacidad - self.front + self.rear + 1

    def mostrarCola(self):
        if self.isEmpty():
            return []
        elementos = []
        i = self.front
        while True:
            elementos.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacidad
        return elementos


# Crear una cola circular con capacidad 5
cola = ColaCircular(5)

cola.enqueue('Aldo')
cola.enqueue('Bianca')
cola.enqueue('Carlos')
print("Cola:", cola.mostrarCola())

print("Primer elemento:", cola.peek())
print("Elimina:", cola.dequeue())
print("Cola después de eliminar:", cola.mostrarCola())

cola.enqueue('Diana')
cola.enqueue('Elena')
print("Cola actual:", cola.mostrarCola())

print("Está llena:", cola.isFull())
print("Tamaño:", cola.size())

# Intentar agregar otro elemento cuando está llena
cola.enqueue('Fernando')  # Debería mostrar que está llena
print(cola.mostrarCola())
print("Está llena:", cola.isFull())
print("Tamaño:", cola.size())

