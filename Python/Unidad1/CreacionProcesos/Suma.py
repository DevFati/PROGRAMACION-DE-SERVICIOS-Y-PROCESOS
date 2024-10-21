#Crea un script en Python llamado suma.py y que reciba como 
# argumentos dos números y devuelva la suma.
# La ejecución en la consola sería: python ( o py) suma.py 3 5 y el resultado 
# La suma es: 8


import sys 
if len(sys.argv)==3: #Por efecto la longitud es 1, al pasarle dos parámetros más pasa a ser 3 
    suma=int(int(sys.argv[1])+int(sys.argv[2]))
    print("La suma es: "+str(suma))
else:
    print("Error, introduce los parámetros correctamente")