from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue):
        self.id = id
        self.posicion_origen = Posicion(origen_x, origen_y)
        self.posicion_destino = Posicion(destino_x, destino_y)
        self.movimiento = Movimiento(origen_x, origen_y, destino_x, destino_y, velocidad)
        self.color = [red, green, blue]
        
        
        
    def __str__(self) -> str:
        return(
            "ID: " + self.id + "\n" +
            "Posicion Origen x: " + str(self.posicion_origen.x) +
            " Posicion Origen y: " + str(self.posicion_origen.y) + "\n" +
            "Posicion Destino x: " + str(self.posicion_destino.x) +
            " Posicion Destino y: " + str(self.posicion_destino.y) + "\n" +
            "Distancia Intermedia: " + str(self.movimiento.distancia) +
            " Velocidad: " + str(self.movimiento.velocidad) + "\n" +
            "Red: " + str(self.color[0]) +
            " Green: " + str(self.color[1]) +
            " Blue: " + str(self.color[2]) + "\n"
        )
        
        
        
    def diccionario_datos(self):
        return{
            "id": self.id,
            "origen_x": self.posicion_origen.x,
            "origen_y": self.posicion_origen.y,
            "destino_x": self.posicion_destino.x,
            "destino_y": self.posicion_destino.y,
            "velocidad": self.movimiento.velocidad,
            "red": self.color[0],
            "green": self.color[1],
            "blue": self.color[2]
        }
        
    
    
#--------------------------------------------------------------------------------------------------------------
        
class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Movimiento:
    def __init__(self, x1, y1, x2, y2, velocidad):
        self.distancia = distancia_euclidiana(x1, y1, x2, y2)
        self.velocidad = velocidad