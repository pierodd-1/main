lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
lenguajes.insert(3, "Go") # Insertar un nuevo elemento "Go" a la lista luega de la posición "3"
lenguajes.insert(0, "C") # Insertar un nuevo elemento "C" a la lista luego de la primera posición
lenguajes.remove("Ruby") # Remover el elemento "Ruby" de la lista

print("PHP" in lenguajes) # Buscar si el elemento "PHP" se encuentra en la lista

print(len(lenguajes))