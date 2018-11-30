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
import time
import random

randfile = open("Random.txt", "w")

start = int(input('Enter lower limit of random numbers: '))
end = int(input('Enter upper limit of random numbers: '))

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(start, end))
    randfile.write(line + '\n')
    print(line)

randfile.close()


# example of selection sort algorithm : needs modification

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])



def selectionSort(a):
    n = len(a)
    for startIndex in range(n):
        minIndex = startIndex
        for ind in range(startIndex+1, n):
            if a[ind] < a[minIndex]:
                minIndex = ind
        swap(a, startIndex, minIndex)

lst = []
with open("Random.txt", "r") as f:
    for line in f:
        lst.append(int(line.strip()))

start_time = time.time()
selectionSort(lst)
end_time = time.time()


file = open("selectionSortResult","w")
for x in lst:
    file.write(str(x)+"\n")
file.close()
print('Sorted Selection Sort List: ', lst)
print('Elapsed time for Selection Sort: {:.20f} seconds'.format(end_time-start_time))




def merge_sort(A):
    """
    Sort list A into order, and return result.
    """
    n = len(A)
    if n==1:
        return A
    mid = n//2   # floor division
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

lst = []
# opens and reads 'Random.txt'
with open("Random.txt", "r") as f:
    for line in f:
        lst.append(int(line.strip()))

start_time = time.time()
lst = merge_sort(lst)
end_time = time.time()


# opens and writes to file 'mergeSortResult.txt'
file = open("mergeSortResult","w")
for x in lst:
    file.write(str(x)+"\n")
# closes 'mergeSortResult.txt'
file.close()
print('Sorted Merge Sort List: ', lst)
print('Elapsed time for Merge Sort: {:.20f} seconds'.format(end_time-start_time))
def mezclaNatural(arr): 
    if len(arr) >1: 
        mitad = len(arr)//2 
        aux1 = arr[:mitad]   
        aux2 = arr[mitad:] 
        mezclaNatural(aux1) 
        mezclaNatural(aux2)  
  
        i = j = k = 0

        while i < len(aux1) and j < len(aux2): 
            if aux1[i] < aux2[j]: 
                arr[k] = aux1[i] 
                i+=1
            else: 
                arr[k] = aux2[j] 
                j+=1
            k+=1
          
        while i < len(aux1): 
            arr[k] = aux1[i] 
            i+=1
            k+=1
          
        while j < len(aux2): 
            arr[k] = aux2[j] 
            j+=1
            k+=1

def mostrar(array): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
 


archivo1=open("Archivo1.txt", "r")
lineaArchivo1=archivo1.readline() 
arr=lineaArchivo1.split(",")
archivo1.close
mostrar(arr) 
mezclaNatural(arr) 
mostrar(arr) 


archivo3=open ("ArchivoSalida.txt", "w")
archivo1=open("Archivo1.txt", "r")
archivo2=open("Archivo2.txt", "r")
repetir=True
  
lineaArchivo1=archivo1.readline() 
lineaArchivo2=archivo2.readline()
 

'''Se realizan comparaciones mientras la bandera no cambie'''
while(repetir):
    if(int(lineaArchivo1)<int(lineaArchivo2)):
        archivo3.write(lineaArchivo1)
        lineaArchivo1=archivo1.readline()
        if(lineaArchivo1==""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo2)
            lineaArchivo2=archivo2.readline()
            while(lineaArchivo2!=""):
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
            repetir=False
    elif(int(lineaArchivo1)>int(lineaArchivo2)):
        archivo3.write(lineaArchivo2)
        lineaArchivo2=archivo2.readline()
        if(lineaArchivo2==""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo1)
            lineaArchivo1=archivo1.readline()
            while(lineaArchivo1!=""):
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
            repetir=False
    else:
        archivo3.write(lineaArchivo1)
        archivo3.write(lineaArchivo2)
        lineaArchivo1=archivo1.readline()
        if(lineaArchivo1==""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo2)
            lineaArchivo2=archivo2.readline()
            while(lineaArchivo2!=""):
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
            repetir=False
        lineaArchivo2=archivo2.readline()
        if(lineaArchivo2==""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo1)
            lineaArchivo1=archivo1.readline()
            while(lineaArchivo1!=''):
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
            repetir=False
archivo2.close
archivo1.close
print("Archivos combinados y ordenados correctamente")
archivo3.close
def ordenamientoQuickSort(lista):
    izq=[]
    centro=[]
    derech=[]
    if len(lista)>1:
        pivote=lista[0]