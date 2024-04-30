#condicional
#Sentencias if y else
# % modulo
numero = int(input("Introduzca un numero entero: "))
if numero % 2 == 0:
    print (f"el numero {numero} es par")
else:
    print (f"el numero {numero} es impar")
# ====================================================================
numero = int(input("Numero: "))
if(numero % 2 == 0) and (numero > 10):
    print (f"El numero {numero} es par y mayor que 10")
# pregunta de nuevo
elif (numero % 2 == 0) and (numero < 10):
    print (f"El numero {numero} es par y menor que 10")
else: 
    print (f"El numero {numero} es el impar")