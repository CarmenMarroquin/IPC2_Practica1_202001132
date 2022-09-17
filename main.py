from re import I
import lista
from nodoLista import NodoLista
import orden
import cola
import nodo as n
import os
import subprocess


cadenaPrincipal= cola.Cola()

def realizarOrden(cola):
    nombre=input("\nIngrese nombre del cliente\n")
    cantidad=input("\ningrese la cantidad de shukos\n")
    print("\nIngrese los ingredientes necesarios:")
    print("para terminar escriba 0")
    print("""     
             1)Salchicha = 1
             2) Chorizo = 2
             3) Salami = 3
             4) Longaniza =4
            5) Costilla = 5\n""")
    salir = True 
    listaIngredientes=lista.listaDoble()
    
    tiempo = 0
    while salir == True:
        ingrediente= input("\nElija los ingredientes: ")
        if int(ingrediente) == 1:
            nodo= NodoLista("Salchicha")
            listaIngredientes.agregar_Final(nodo)
            tiempo =2+tiempo
        elif int(ingrediente) == 2:  
            nodo1= NodoLista("Chorizo")
            listaIngredientes.agregar_Final(nodo1)  
            tiempo =3+tiempo
        elif int(ingrediente) == 3:  
            nodo2= NodoLista("Salami")
            listaIngredientes.agregar_Final(nodo2) 
            tiempo =1.4+tiempo
        elif int(ingrediente) == 4:  
            nodo3= NodoLista("Longaniza")
            listaIngredientes.agregar_Final(nodo3)    
            tiempo =4+tiempo  
        elif int(ingrediente) == 5:  
            nodo4= NodoLista("Costilla")
            listaIngredientes.agregar_Final(nodo4)
            tiempo =6+tiempo
        else: 
            salir = False
             
    
    ordenCreada= orden.Orden(nombre,cantidad,listaIngredientes,tiempo*int(cantidad))               
    nodoTotal=n.Nodo(ordenCreada)
    cola.encolar(nodoTotal)
    menu(cola)
        
def verOrden(cadena):
    #listaTiempo= lista.listaDoble()
    
    tiempoGlobal = 0
    grafi = 'digraph orden{\n'\
        'rankdir = "LR"\n'\
        'node[shape="folder" style="filled" fillcolor="white"]\n' 
    for i in range(cadena.tamaño):
        cadena1=cadena.buscar(i)
        nombre=cadena1.dato.datos
        canti=cadena1.dato.cantidad
        tiempo1= cadena1.dato.tiempo
        tiempoOrdenActual=int(tiempo1) * int(canti)
        tiempoGlobal += tiempo1
        #nodotiempo= NodoLista(tiempoOrdenActual)
        #listaTiempo.agregar_Final(nodotiempo) 
        
        #tiempoActual= listaTiempo.buscar_nodo(i).dato
        print("\nNombre: "+nombre)
        print("\nCantidad: "+str(canti))
        print("\ntiempo multi: "+str(tiempoGlobal))
        print("\nIngredientes: ")
        ingre = cadena1.dato.shuko
        for j in range(ingre.tamanio):
            ingrediente1=ingre.buscar_nodo(j)
            ingredi=ingrediente1.dato
            print(ingredi)
            print("-------------------------")
        texto = grafico(nombre,canti,tiempoGlobal,ingredi,i)
        grafi = grafi + texto
    
    conexiones = ''
    for i in range(cadena.tamaño - 1):
        conexiones += 's' + str(i) +'->' + 's' + str(i+1)
    conexiones += '\n'
    
    grafi += conexiones + '\n}'  
    
    archivo = open('La_Orden.dot', 'w', encoding='utf-8')
    archivo.write(grafi)
    archivo.close()
    subprocess.run(['dot', '-Tsvg', 'La_Orden.dot', '-o', 'La_Orden.svg'])
    os.startfile('La_Orden.svg')    
    menu(cadena)   
  
            
        
def entregar(cadena):
    
    tiempoGlobal = 0
    grafi = 'digraph orden{\n'\
        'rankdir = "LR"\n'\
        'node[shape="folder" style="filled" fillcolor="white"]\n'
    entrega= cadena.desencolar().dato
    nombre = entrega.datos
    canti= entrega.cantidad
    tiempo = entrega.tiempo
    
    tiempoGlobal += tiempo
    ingre = entrega.shuko
    for i in range(ingre.tamanio):
        ingrediente1=ingre.buscar_nodo(i)
        ingredi=ingrediente1.dato
        print(ingredi)
        print("-------------------------")
    texto = grafico(nombre,canti,tiempoGlobal,ingredi,i)
    grafi = grafi + texto    
    
    conexiones = ''
    for i in range(cadena.tamaño - 1):
        conexiones += 's' + str(i) +'->' + 's' + str(i+1)
    conexiones += '\n'
    
    grafi += conexiones + '\n}'  
    
    archivo = open('La_Orden.dot', 'w', encoding='utf-8')
    archivo.write(grafi)
    archivo.close()
    subprocess.run(['dot', '-Tsvg', 'La_Orden.dot', '-o', 'La_Orden.svg'])
    os.startfile('La_Orden.svg')    
    menu(cadena) 

           
def grafico(nombre,cantidad,tiempo,ingredientes,indice):
    
    nombre1 = nombre
    cantidad1 = cantidad
    tiempo1 = tiempo
    ingredientes1 = ingredientes

    label='s'+str(indice)+' [label="Nombre:'+nombre1+' | Cantidad de shucos: ' +str(cantidad1)+ '| Tiempo: ' +str(tiempo1)+ '| '+ingredientes1+'"]\n'
    return label
               
            

    
def menu(cadenaPrincipal):
    print("\ningrese 1 si de desea ingresar una orden")
    print("ingrese 2 si desea ver los pedidos")
    print("ingrese 3 para entregar orden ")
    print("ingrese 4 para datos  ")
    print("ingrese 5 si desea salir del menu\n")
    eleccion= input("Selecciona una opcion: ")
    if int(eleccion) == 1:
        realizarOrden(cadenaPrincipal)    
    elif int(eleccion) ==2:
        verOrden(cadenaPrincipal)   
    elif int(eleccion) == 3:
        entregar(cadenaPrincipal)
    elif int(eleccion) == 4:
        print("Nombre: Carmen María Marroquín Llamas\n")
        print("Carné: 202001132\n")
        menu(cadenaPrincipal)
    elif   int(eleccion) == 5:  
        pass
          
          
        
if __name__ == "__main__":
    print("\n-------- Menu -------")
    
    menu(cadenaPrincipal)
    