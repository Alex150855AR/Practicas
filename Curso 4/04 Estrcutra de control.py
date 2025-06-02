"""

Las estructuras condicionales nos permiten ejecutar diferentes bloques de código según se cumpla o no una determinada condición. 
En Python, las estructuras condicionales más utilizadas son if, if-else y if-elif-else.

"""

" if "

" if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente " 

"""
if condicion:

   # Bloque de código a ejecutar si la condición es verdadera
   instrucciones  

"""
edad =  18

if edad >= 18:
    print ("Eres mayor de edad. ")

##################################################################################################

" if - else "

edad = 15


if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")

##################################################################################################

" if - elif - else "

" La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente" 
"""

if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones

"""

calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")

