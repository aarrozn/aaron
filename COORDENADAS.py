# Inicializar variables
num_materias = int(input("Ingrese el número de materias: "))
suma_calificaciones = 0

# Bucle para ingresar el nombre y la calificación de cada materia
for i in range(num_materias):
    materia = input(f"Ingrese el nombre de la materia {i + 1}: ")
    calificacion = float(input(f"Ingrese la calificación de {materia}: "))
    suma_calificaciones += calificacion

# Calcular el promedio
promedio = suma_calificaciones / num_materias

# Mostrar el promedio
print("El promedio de las calificaciones del semestre es:", promedio)
