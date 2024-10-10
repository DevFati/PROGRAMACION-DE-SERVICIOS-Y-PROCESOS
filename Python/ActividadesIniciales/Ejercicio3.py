# Escriba un programa que simule un juego en el que dos jugadores (Gloria y
#Héctor) sacan tres cartas al azar del 1 al 10. Gana el jugador que obtenga la mayor
#puntuación total, siempre que no se pase de quince, en cuyo caso el jugador pierde..
import random
Gloria=list()
Hector=list()
sumaG=0
sumaH=0

for i in range(0,3):
   
    Gloria.append(random.randint(1,10))
    Hector.append(random.randint(1,10))

for i in range(0,3):
    sumaG=sumaG+Gloria[i]
    sumaH=sumaH+Hector[i]

print("JUEGO DEL QUINCE")
print("Gloria ha sacado un "+str(Gloria[0])+", un "+str(Gloria[1])+" y un "+str(Gloria[2])+".")
print("Héctor ha sacado un "+str(Hector[0])+", un "+str(Hector[1])+" y un "+str(Hector[2])+".")

if(sumaG<= 15 and sumaH <=15):
    if(sumaG>sumaH):
        print("Ha ganado Gloria")
    else:
        print("Ha ganado Hector")
else:
    if(sumaG>15 and sumaH<=15):
        print("Gloria pierde")
    elif(sumaH>15 and sumaG<=15):
        print("Hector pierde")
    else:
        print("Gloria y Hector pierden")