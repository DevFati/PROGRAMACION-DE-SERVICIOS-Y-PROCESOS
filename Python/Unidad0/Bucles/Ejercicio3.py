# Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida
#esos nu meros, y muestre un mensaje cada vez que un nu mero no sea mayor que el
#primero.


m=int(input("¿Cuantos numeros se van a introducir?: "))

for i in range(0,m):
    num=int(input("Introduce un numero: "))
    if(i==0):
        n=num
    else:
        if(num<=n):
            print("El numero "+str(num)+" no es mayor que "+str(n))
    