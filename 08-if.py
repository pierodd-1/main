puntaje = input("Ingrese Puntaje: ")

if float(puntaje) >= 90: 
    print("Aprobado con honores")
elif float(puntaje) < 90 and float(puntaje) >= 60: 
    print("Nota aprobatoria")
else:
    print("Nota desaprobatoria")

puntaje = 93

if puntaje >= 95:
    print("Aprobado con honores")
elif puntaje >= 50:
    print("Alumno aprobado")
else:
    print("Reprobado")
