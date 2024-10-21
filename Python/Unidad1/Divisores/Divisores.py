#Crea un script en Python llamado divisores.py y que reciba como argumento un número y 
# devuelva los divisores de ese número. 


import sys 
if len(sys.argv)==2:
    lista=list()

    for i in range (1,int(sys.argv[1])+1):
        if(int(sys.argv[1])%i==0):
            lista.append(i)
    
    print(str(sys.argv[1])+" tiene "+str(len(lista))+" divisores: "+str(lista))
       
else:
    print("Error, introduce los parámetros correctamente")