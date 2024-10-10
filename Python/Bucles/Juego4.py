# Escriba un programa que pida un número de dados, un valor a objetivo y que tire
#después el número de dados indicado. El jugador gana si saca el valor ganador.

import random
salir=True
resultados=""
gana=False
while(salir):
    print("OBTENER VALOR(2)")
    m=int(input("Número de dados: "))
    if(m<=0):
        print("¡Imposible!")
    else:
        valor=int(input("Valor a conseguir: "))
        if valor<1 or valor>6:
            print("¡Imposible conseguir un "+str(valor)+"!")
        else:
            for i in range (0,m):
                tirada=random.randint(1,6)
                resultados=resultados+str(tirada)+" "
                if(tirada == valor):
                    gana=True
            print("Dados: "+resultados)
            if gana:
                print("El jugador ha ganado.")
            else:
                print("El jugador ha perdido.")
            salir=False