import math

# Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calcular la distancia utilizando la fórmula
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar la distancia calculada
print("La distancia entre los puntos es:", distancia)
