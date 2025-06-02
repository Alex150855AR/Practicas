" For El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente: "

"""

for variable in secuencia:

    # Bloque de código a repetir
    instrucciones

"""

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)



" While , se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:"

"""

while condicion:

    # Bloque de código a repetir
    instrucciones

"""

contador = 0


while contador < 5:

    print(contador)
    contador += 1

"Control de bucles"

" Break, se utiliza para salir prematuramente de un bucle"

contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

"Continue, se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración."

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)


"Pass, es una operación nula que no hace nada. Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción."

for i in range(5):
    pass

