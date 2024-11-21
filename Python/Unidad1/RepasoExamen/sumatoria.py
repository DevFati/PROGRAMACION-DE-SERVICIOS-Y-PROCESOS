import sys
if len(sys.argv)==2:
    n=int(sys.argv[1])
    if(n<=0):
        print("Error, el numero tiene que ser mayor que 0")
    else:
        total=0
        for i in range(1,n+1):
            total=total+i

        print(total)
else:
    print("Error, introduce los parámetros correctamente")