#Escriba un programa que pida un número de dados y tire esa cantidad de dados.
#El primer jugador obtiene un punto por cada dado par. El segundo jugador obtiene
#un punto por cada dado impar. El jugador que saque más puntos, gana.

import random
salir=True
resultados=list()
pares=0
nones=0
while(salir):
    print("PARES Y NONES")
    m=int(input("Número de dados: "))
    if(m<=0):
        print("¡Imposible!")
    else:
        for i in range(0,m):
            valor=random.randint(1,6)
            resultados.append(valor)
            if valor%2==0:
                pares+=1
            else:
                nones+=1
        print("Dados: ",*resultados,sep=" ")
        if pares > nones:
            print("Ha ganado el jugador de los pares.")
        elif nones > pares:
            print("Ha ganado el jugador de los impares")
        else:
            print("Han empatado")   
        salir=False 