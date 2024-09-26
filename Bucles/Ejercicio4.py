#Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida
#esos nu meros, y muestre un mensaje cada vez que un nu mero no sea mayor que el
#anterior.

m=int(input("¿Cuantos numeros se van a introducir?: "))

for i in range(0,m):
    actual=int(input("Introduce un numero: "))
    if(i>0):
        if(actual<=n):
            print("El numero "+str(actual)+" no es mayor que el numero anterior que es "+str(n))     
    
    n=actual
    