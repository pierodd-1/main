numero = int(input("Ingrese número: "))
if numero == 1:
    print("El número no es valido")
else:
    divisores = 1
    for i in range (2, numero + 1):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        print("El número es primo")
    else:
        print("El número no es primo")