#. Escriba un programa que pida un nu mero y a continuacio n escriba la lista de
#todos los divisores del nu mero (incluidos el uno y e l mismo).

n=int(input("Digame un numero: "))

lista=list()

for i in range (1,n+1):
    if(n%i==0):
        lista.append(i)

print(str(n)+" tiene "+str(len(lista))+" divisores: "+str(lista))