import nodo 
class Cola:
    def __init__(self):
        self.tamaño=0
        self.cabeza=None
        self.ultimo=None
   
    def vacia(self):
        if self.tamaño == 0:
            return True
        else: return False
        
    def encolar(self,valor):
        
        if self.vacia():
            self.cabeza = valor
            self.ultimo = valor
            self.tamaño +=1
        else:
            self.ultimo.siguiente= valor
            self.ultimo= valor   
            self.tamaño +=1
        
    def desencolar(self):
        if self.vacia():
            return False
        
        else:
            self.tamaño -=1
            aux= self.cabeza
            self.cabeza = self.cabeza.siguiente
            return aux
    
    def buscar(self,posicion):
        aux=self.cabeza
        posicionAuxiliar=0
        
        while posicionAuxiliar < posicion:
            if aux.siguiente is not None:
                aux=aux.siguiente 
            posicionAuxiliar +=1
        
        return aux 
        
               
        
        