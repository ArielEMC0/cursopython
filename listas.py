#Listas 1
impares = [1, 3, 5, 7, 9 , 11, 13, 15, 17, 19]
#          0  1  2  3  4   5   6   7   8   9
#            -9 -8 -7 -6  -5  -4  -3  -2  -1
print (impares)
print (type(impares))
print (impares[4])
print (impares[-6])
#punteros de acceso desde el inicio imporime los 4 primeros elementos
print (impares[:4])
#punteros de acceso desde el punto hatas el final, despues el elemento 4, obvia el 4to elemento y imprime toda la lista
print (impares[4:])
#despues del elemento 4 hasta el elemento 6
print (impares[4:6])
#izquierda a derecha (desde -4 hasta -1)
print (impares[-4:-1])
# print (impares[-1:-4]) error
#============================================================================================================================
lista_alfanumerica = ["a", 1 , "b", 2, "c", 3, "d"]
print (lista_alfanumerica)
print (len(lista_alfanumerica))
medio = len (lista_alfanumerica) // 2
print (lista_alfanumerica[medio])
#============================================================================================================================
nombre = "Ariel"
nota = 90
print (f"Tu nombre es: {nombre} Tu nota es: {nota}")
#============================================================================================================================
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# funcion .reverse() no devuelve valor
# len() devuelve un valor
tamaño = len(impares)
print (tamaño)
revertido = impares.reverse()
print (impares)
print (revertido)

desordenado = [5, 2, 6, 9 ,1, 3, 7]
desordenado.sort()
print (desordenado)
#============================================================================================================================
#Matriz = combinacion de listas
matriz = [
    [1, 2, 3, 4, 5],         #posicion 0
    [6, 7, 8, 9, 10],        #posicion 1   
    [11, 12, 13, 14, 15]     #posicion 2
]
print (matriz)
#[1] posicion (linea) y [2] posicion de elemnto de la lista (columna)
print (matriz[1][2])