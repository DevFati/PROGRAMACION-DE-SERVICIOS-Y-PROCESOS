import sys

if len(sys.argv)==2:

    n=int(sys.argv[1])
    if(n<0):
        print("Error, el número tiene que ser mayor o igual que 0.")
    else:
        total=1
        for i in range(1,n+1):
            total=total*i

        print("El factorial de " +str(n)+" es "+str(total))
else:
   print("Error, introduce el número correcto de parámetros.")