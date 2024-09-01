temperatura = float(input("Ingrese temperatura "))
escala = input("¿La temperatura está en Fahrenheit (f) o Celcuis (c)?: ").lower()
if escala == "c":
    fahreinheit = (temperatura * 9 /5 + 32)
    print("La temperatura es de ", fahreinheit, "fahreinheit")
elif escala == "f":
    celcius = ((temperatura - 32) * 5 / 9)
    print("La temperatura es de ", celcius, "fahreinheit")
else:
    print("Escala incorrecta")