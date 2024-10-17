#Escriba un programa que permita crear una lista de palabras y que, a
#continuacio n, pida una palabra y diga cua ntas veces aparece esa palabra en la lista.

m=int(input("Dígame cuántas palabras tiene la lista: "))

lista=list()

for i in range(0,m):
    r=input("Digame la palabra "+str(i+1)+":")
    lista.append(r)

print("La lista creada es: "+str(lista))

buscar=input("Dígame la palabra a buscar: ")

cont=lista.count(buscar)
print("La palabra "+buscar+" aparece "+str(cont)+" veces en la lista.")