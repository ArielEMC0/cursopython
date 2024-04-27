#1
#str cadena de texto
mi_variable = input("Escribe tu valor: ")
print ("tu valor es: " + mi_variable)
print (type(mi_variable))

#2
#3 opciones NO se puede concaternar un string y un int (letra y entero)
#a_transformado = int (a) 
#b = int (b)
#int = solo valores numericos
#str = ayuda a concatenar letras con variables (enteros)
print ("hola " + str(5))
a = input ("Primer numero: ")
b = input ("Segundo numero: ")
c = int(input("Tercer numero: "))
a_transformado = int(a)
b = int (b)
resultado = a_transformado + b + c 
print ("Resultado: " + str(resultado))

#3