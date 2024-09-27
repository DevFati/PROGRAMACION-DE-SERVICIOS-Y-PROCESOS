#Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida esos
#nu meros, y escriba el mayor, el menor y la media aritme tica. Recuerda que la media
#aritme tica de un conjunto de valores es la suma de esos valores dividida por la cantidad de
#valores.

m=int(input("¿Cuantos numeros se van a introducir?: "))
suma=0
lista=list()
for i in range(0,m):
    n=float(input("Introduce un numero: "))
    lista.append(n)
    suma=suma+n

print("El mayor es: "+str(max(lista)))     
print("El menor es: "+str(min(lista))) 
print("La media aritmética es: "+str(suma/len(lista)))    
  