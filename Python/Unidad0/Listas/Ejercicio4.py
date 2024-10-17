#Escriba un programa que permita crear una lista de palabras y que, a
#continuacio n, pida una palabra y elimine esa palabra de la lista.

m=int(input("Dígame cuántas palabras tiene la lista: "))

lista=list()
listan=list()
for i in range(0,m):
    r=input("Digame la palabra "+str(i+1)+":")
    lista.append(r)

print("La lista creada es: "+str(lista))

eliminar=input("Palabra a eliminar: ")

for i in range(0,len(lista)):
    if(lista[i]!=eliminar):
        listan.append(lista[i])

print("La lista es ahora: "+str(listan))
