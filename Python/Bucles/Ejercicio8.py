#. Escriba un programa que pregunte cuantos nu meros se van a introducir, pida esos
#nu meros (que puedan ser decimales) y calcule su suma.

m=int(input("¿Cuantos numeros se van a introducir?: "))
suma=0
for i in range(0,m):
    n=float(input("Introduce un numero: "))
    suma=suma+n

print("La suma total de los numeros introducidos es: "+str(suma))
       
  