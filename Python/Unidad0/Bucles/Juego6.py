#. Escriba un programa que pida un número de dados y tire esa cantidad para dos
#jugadores. El jugador que saque el valor más alto, gana.

import random
salir=True
resultados1=list()
resultados2=list()
while(salir):
    print("EL DADO MÁS ALTO(2)")
    m=int(input("Número de dados: "))
    if(m<=0):
        print("¡Imposible!")
    else:
        for i in range (0,m):
            resultados1.append(random.randint(1,6))
            resultados2.append(random.randint(1,6))

        print("Jugador 1:",*resultados1, sep=" ")
        print("Jugador 2:",*resultados2, sep=" ")
        if(max(resultados1)>max(resultados2)):
            print("Ha ganado el jugador 1")
        elif (max(resultados2)>max(resultados1)):
            print("Ha ganado el jugador 2")
        else:
            print("Han empatado")
        salir=False