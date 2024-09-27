#. Escriba un programa que pida dos nu meros enteros y escriba la suma de todos los
#enteros desde el primer nu mero hasta el segundo.

suma=0
while(True):
    n=int(input("Introduce el primer numero: "))
    m=int(input("Introduce el segundo numero: "))
    if(n>m):
        print("El primer numero tiene que ser menor que el segundo!")
    else:
        for j in range (n,m+1):
            suma=suma+j
        print("La suma de todos los enteros desde "+str(n)+" hasta "+str(m)+" es: "+str(suma))
        break

   

       
  