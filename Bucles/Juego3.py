#3. Escriba un programa que pida un número de jugadores y un valor que se pretende
#conseguir. A continuación, se tira un dado para cada jugador y el programa debe
#decir qué jugador ha conseguido obtener el valor.

import random
salir=True

while(salir):
    print("OBTENER VALOR(1)")
    m=int(input("Número de jugadores: "))
    if(m<=0):
        print("¡Imposible!")
    else:
        valor=int(input("Valor a conseguir: "))
        if valor<1 or valor>6:
            print("¡Imposible conseguir un "+str(valor)+"!")
        else:
            for i in range (0,m):
                tirada=random.randint(1,6)
                if(tirada == valor):
                    print("Jugador "+str(i+1)+": "+str(tirada)+" CONSEGUIDO")
                else:
                    print("Jugador "+str(i+1)+": "+str(tirada))
            salir=False