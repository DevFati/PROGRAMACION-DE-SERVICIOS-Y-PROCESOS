#Escriba un programa que pida un nu mero entero mayor que cero y que escriba
#sus divisores.


while(True):
    m=int(input("Introduce un numero entero mayor que cero: "))
    if(m>0):
        for i in range(1,m+1):
            if(m%i==0):
                print(i)
        break
    