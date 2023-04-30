from particula import Particula
import json

class Registro_particulas:
    def __init__(self):
        self.particulas = []
        
        
        
    def __str__(self):
        return " ".join(str(p) + "\n" for p in self.particulas)
        
        
    
    def __len__(self):
        return(len(self.particulas))
    
    
    
    def __iter__(self):
        self.count = 0
        return self
    
    
    
    def __next__(self):
        if self.count < len(self.particulas):
            particula = self.particulas[self.count]
            self.count += 1
            return particula
        
        else:
            raise StopIteration
    
    
            
    def agregar_particula_inicio(self, particula:Particula):
        self.particulas.insert(0, particula)
    
    
    
    def agregar_particula_final(self, particula:Particula):
        self.particulas.append(particula)
        
        
        
    def imprimir_particulas(self):
        for p in self.particulas:
            print(p)
    
        
        
    def guardar_particulas(self, direccion):
        try:
            with open(direccion, "w") as archivo:
                lista = [particula.diccionario_datos() for particula in self.particulas]
                json.dump(lista, archivo, indent = 4)
                return 1
            
        except:
            return 0
    
    
    
    def cargar_particulas(self, direccion):
        try:
            with open(direccion, 'r') as archivo:
                lista = json.load(archivo)
                self.particulas = [Particula(**particula) for particula in lista]
                return 1
        
        except:
            return 0