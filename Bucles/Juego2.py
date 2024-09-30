
#Escriba un programa que pida un número de jugadores y tire un dado para cada
#jugador.


import random;



salir=True
while(salir):
    print("TIRADAS DE DADO")

    n=int(input("Numero de jugadores: "))
    if(n<=1):
        print("¡Imposible!")
    else:
        for i in range (0,n):
            print("Jugador "+(str(i+1))+": "+str(random.randint(1,6)))
        salir=False