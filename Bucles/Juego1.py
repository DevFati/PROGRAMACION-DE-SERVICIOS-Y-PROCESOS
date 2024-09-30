#Escriba un programa que pida un número de dados y muestre los valores de ese
#número de dados, al azar.
import random
salir=True 
resultados=list()
while(salir):
    print("TIRADA DE DADOS")
    n=int(input("Número de dados: "))
    if(n<=0): 
        print("¡Imposible!")
    else:
        for i in range (0,n):
            resultados.append(random.randint(1,6))
        print("Dados: "+resultados)
        salir=False
//CORREGIRRRRRR