import random
def llenaLista(n):
    lista = [random.randint(0,100) for _ in range(n)]
    return lista
def comparador(init,fin,compas,cambios,recors):
    print("tiempo: "+(fin-init))
    print("comparaciones: "+compas)
    print("cambios: "+cambios)
    print("recorridos: "+recors)
def mostrar(alvs):
    print(alvs)
def burbuja():
    print("alkv")
    
def ordenamientoPorSeleccion(numeros):
    for recorrido in range(len(numeros)-1, 0, -1):
        posicionDelMayor = 0
        for recorrido2 in range (1, recorrido+1):
            if numeros[recorrido2]> numeros[posicionDelMayor]:
                posicionDelMayor = recorrido2
                
        aux = numeros[recorrido]
        numeros [recorrido] = numeros[posicionDelMayor]
        numeros[posicionDelMayor] = aux

def ordenamientoInsercion(lista):
    for indice in range(1,len(lista)):
        valor=lista[indice]
        i=indice-1
        while i>=0:
            if valor<lista[i]:
                lista[i+1]=lista[i]
                lista[i]=valor
                i=i-1
            else:
                break
def ordenamientoQuickSort(lista):
    izq=[]
    centro=[]
    derech=[]
    if len(lista)>1:
        pivote=lista[0]