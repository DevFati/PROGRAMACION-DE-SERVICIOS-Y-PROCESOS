#Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida
#esos nu meros, y diga al final cua ntos han sido pares y cua ntos impares.

m=int(input("¿Cuantos numeros se van a introducir?: "))
contadorP=0
contadorI=0
for i in range(0,m):
    n=int(input("Introduce un numero: "))
    if(n%2==0):
        contadorP+=1
    else:
        contadorI+=1

print("Se han introducido "+str(contadorP)+" numeros pares y "+str(contadorI)+" numeros impares")
       
  