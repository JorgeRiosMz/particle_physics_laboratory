from math import sqrt, pow

def distancia_euclidiana(x1, x2, y1, y2):
    distancia = sqrt(pow((x1 - x2), 2) + pow((y1 - y2),2))
    return distancia