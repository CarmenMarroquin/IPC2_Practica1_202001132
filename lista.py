import nodoLista as nl
class listaDoble:

    def __init__(self):
        self.primero= None
        self.ultimo=None
        self.tamanio=0


    def vacio(self):
        if self.tamanio == 0:
            return True

    
    def agregar_Final(self,dato):
        if  self.vacio()== True:
            self.primero = dato
            self.ultimo = dato 
            self.tamanio +=1
        else:
            
            self.ultimo.siguiente=dato   
            dato.anterior=self.ultimo
            self.ultimo=dato
            self.tamanio +=1
            
    def buscar_nodo(self,posicion)-> nl.NodoLista:
        aux=self.primero
        posicion_aux=0
        
        while posicion_aux < posicion:
            if aux.siguiente is not None:
                aux=aux.siguiente 
            posicion_aux +=1
        
        return aux    
    