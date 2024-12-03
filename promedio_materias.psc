Algoritmo promedio_materias
    Definir num_materias, suma_calificaciones, promedio, calificacion Como Real
    Definir i Como Entero
    Definir materia Como Cadena
	
    suma_calificaciones <- 0
	
    Escribir "Ingrese el número de materias:"
    Leer num_materias
	
    Para i <- 1 Hasta num_materias Hacer
        Escribir "Ingrese el nombre de la materia ", i, ":"
        Leer materia
        
        Escribir "Ingrese la calificación de ", materia, ":"
        Leer calificacion
        
        suma_calificaciones <- suma_calificaciones + calificacion
    FinPara
	
    promedio <- suma_calificaciones / num_materias
	
    Escribir "El promedio de las calificaciones del semestre es: ", promedio
FinAlgoritmo

