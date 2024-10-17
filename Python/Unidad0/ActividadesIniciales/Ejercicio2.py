#Escriba un programa que simule un juego en el que dos jugadores (Carmen y
# David) tiran dos dados. El que saque mayor puntuacio n total, gana. Si la puntuacio n
# total coincide, gana quien haya sacado el dado con el valor ma s alto. Si el valor ma s
# alto tambie n coincide, empatan. Si puntuacio n total coincide, gana quien haya 
# sacado el dado con el valor ma s alto. Si el valor ma s alto tambie n coincide,
# empatan.


import random

print("JUEGO DE DADOS")
David1=random.randint(1,6)
Carmen1=random.randint(1,6)
David2=random.randint(1,6)
Carmen2=random.randint(1,6)
totalD=David1+David2
totalC=Carmen1+Carmen2
print("Carmen ha sacado un "+str(Carmen1)+" y un "+str(Carmen2))
print("David ha sacado un "+str(David1)+" y un "+str(David2))

if totalD>totalC:
    print("Ha ganado David")
elif totalD < totalC:
   
    print("Ha ganado Carmen")
elif totalC == totalD:
    if(max(David1,David2)> max(Carmen1,Carmen2)):
        print("Ha ganado David")
    elif(max(David1,David2)< max(Carmen1,Carmen2)):
        print("Ha ganado Carmen")
    elif(max(David1,David2) == max(Carmen1,Carmen2)):
        print("Han empatado")
 
