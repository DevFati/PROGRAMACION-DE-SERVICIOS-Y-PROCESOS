#Escriba un programa que permita crear una lista de palabras. Para ello, el programa
#tiene que pedir un nu mero y luego solicitar ese nu mero de palabras para crear la lista. Por
#u ltimo, el programa tiene que escribir la lista.

m=int(input("Dígame cuántas palabras tiene la lista: "))

lista=list()

for i in range(0,m):
    r=input("Digame la palabra "+str(i+1)+":")
    lista.append(r)

print("La lista creada es: "+str(lista))