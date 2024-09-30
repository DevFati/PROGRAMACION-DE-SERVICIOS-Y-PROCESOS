#Listas 

lista=["Juan",31,True]
print(len(lista))
print(lista[2])

lista.append(8)
lista.insert(1,"hola")
print(lista)

lista2=["Hola",1]
print(lista+lista2)
print(lista*2)
lista.remove(True)
print(lista)

#Diccionario 

dicc={"Maria":25,
      "Jose":23}

print(dicc)

print(dicc.values())
print(dicc.keys())


#Conjuntos 

conj=set([9,8,1,2,3,3,3,4,5,5,5])
print(conj)


t="hola",3,"si"
print(t)

print(t[1:2])

print(t[-2])