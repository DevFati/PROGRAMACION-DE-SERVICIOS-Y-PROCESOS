#Escriba un programa que permita crear una lista de palabras y que, a
#continuacio n, pida dos palabras y sustituya la primera por la segunda en la lista.

m=int(input("Dígame cuántas palabras tiene la lista: "))

lista=list()

for i in range(0,m):
    r=input("Digame la palabra "+str(i+1)+":")
    lista.append(r)

print("La lista creada es: "+str(lista))

palabra1=input("Sustituir la palabra : ")
palabra2=input("por la palabra: ")

for i in range(0,len(lista)):
    if(lista[i]==palabra1):
        lista[i]=palabra2

print("La lista es ahora: "+str(lista))
