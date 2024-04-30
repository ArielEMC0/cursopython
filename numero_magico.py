'''
Guarda en una variable **numero_magico** el valor **12345679** (sin el 8)
Lee por pantalla otro **numero_usuario**, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo (**numero_usuario**)
Multiplica el **numero_magico** por el **numero_usuario** en sí mismo (**numero_magico**)
Finalmente muestra el valor final del **numero_magico** por pantalla
el operador *= multiplica por si mismo
tener cuidado con multiplicar texto con cadenas (numeros)
f = resetea cadenas
definir lista (1,2,3,4....) y [1,2,3,4...] "conjuntos" ("a","b","c"....) ("a", 1, "b", 3 0-5, "b") indices o posiciones
'''
numero_magico = 12345679
numero_usuario = int(input("Introduzca un numero en el rango del 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print (f"El valor final del numero_magico es: " + str(numero_magico)) 
# o tambien = print (f"El valor final del numero_magico es: {numero_magico}") 