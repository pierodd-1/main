texto = "Hola Mundo"
print(texto.upper()) # Mayusculas
print(texto.lower()) # Minusculas
print(texto.find("Mun")) # Encontrar (posición)
print(texto.find("mun")) # Econtrar (posición invalida)
print(texto.replace("Hola", "Adios")) # Reemplazar
nuevoTexto = texto.replace("Hola", "Adios") # Definir nueva variable reemplazando "texto" por "nuevoTexto"
print("texto1:", texto, "texto2:", nuevoTexto) # Imprimir Variable con texto todo junto (,)
print("texto1:", texto) 
print("texto2:", nuevoTexto) # Imprimir Variable por separado
print("Mundo" in texto) # Buscar si está el elemento "Mundo" en la Variable "texto" (True)
print("Adios" in texto) # Buscar si está el elemento "Adios" en la Variable "texto" (False)
print("Adios" in nuevoTexto) # Buscar si está el elemento "Adios" en la Variable "nuevoTexto"
print("Adios" in nuevoTexto) # Buscar si está el elemento "Adios" en la Variable "nuevoTexto"
