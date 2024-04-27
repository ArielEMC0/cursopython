#cuidado con el interprete (solo reconoce codigo)
#cerrar el interprete de la terminal con exit() antes de correr el codigo
#1
print ("Hola Ariel")
#2
numero =  5
print (numero)
print (type(numero))
#3
saludo = "Hola Ariel"
#print (saludo)
print (type(saludo))
#4
decimal = 5.5
#print (decimal)
print (type(decimal))
'''
Comentario con comillas simples o dobles o #
'''
'''
Este codigo
imprime
saltos de
linea
'''
#salto de lineas
print ("""Hola
desde
LASIN""")
'''
Imprimir sin tabular
print ('Ariel 60')
print ('Evelin 100')
print ('Pedro 70')
print ('Sandra 50')
'''
#Imprimir tabulares (ordenados) 'castear'
print ('Ariel\t\t60')
print ('Evelin\t\t100')
print ('Pedro\t\t70')
print ('Sandra\t\t50')
#\n saltos en una sola linea
print ("Hola \n desde \n LASIN")
#Errores en \n y \t (si el nombre tuviese t o n delante del backslash \ puede saltarse
#entonces se debera poner r antes de las comillas)
#print ("C:\home\nilda\trabajo\datos.csv")
#GIT funciona de forma local como programa en cambio github
print (r"C:\home\nilda\trabajo\datos.csv")