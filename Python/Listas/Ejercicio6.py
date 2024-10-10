#. Escriba un programa que pida un nu mero y a continuacio n escriba la lista de
#todos los nu meros primos hasta e l.


n=int(input("Digame un numero: "))

lista=list()

for i in range (1,n+1):
    cont=0
    for j in range(1,i+1):
        if(i%j==0):
            cont+=1
    if(cont==2):
        lista.append(i)



print(str(lista))
print("Primos hasta "+str(n)+": ",*lista,sep=" ")
    