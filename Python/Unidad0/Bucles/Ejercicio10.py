#Mejora el programa anterior haciendo que el programa escriba la suma realizada

suma=0
while(True):
    n=int(input("Introduce el primer numero: "))
    m=int(input("Introduce el segundo numero: "))
    if(n>m):
        print("El primer numero tiene que ser menor que el segundo!")
    else:
        cadena=""
        for j in range (n,m+1):
            suma=suma+j
            if(j==m):
                cadena=cadena+str(j)
            else:
                cadena=cadena+str(j)+"+"
        print(cadena+"="+str(suma))
        break

   