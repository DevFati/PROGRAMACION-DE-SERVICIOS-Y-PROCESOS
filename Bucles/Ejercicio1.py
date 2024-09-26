#Escriba un programa que pida dos numeros enteros y escriba que numeros son pares y
#cuales impares desde el primero hasta el segundo.

lista=list()

while (True):
    print("PARES E IMPARES")
    n=int(input("Escriba un número entero: "))
    m=int(input("Escriba un número entero mayor o igual que " +str(n)+": "))
    
    if(m<n):
        print("¡Le he pedido un número entero mayor o igual que "+str(m)+"!")
    else:
        
        for i in range(n,m+1):
            if(i%2==0):
                print("El numero "+str(i)+" es par")
            else:
                print("El numero "+str(i)+" es impar")
        break




    


    