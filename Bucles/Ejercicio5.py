#Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida
#esos nu meros y escriba cua ntos negativos ha introducido.

m=int(input("¿Cuantos numeros se van a introducir?: "))
contador=0
for i in range(0,m):
    n=int(input("Introduce un numero: "))
    if(n<0):
        contador+=1

print("Se han introducido "+str(contador)+" numeros negativos")
       
    
    