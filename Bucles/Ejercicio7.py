#Escriba un programa que pida un nu mero entero mayor que 1 y que escriba si el
#nu mero es un nu mero primo o no.

while(True):
    num=int(input("Introduce un numero entero mayor que 1: "))

    if(num>1):
        contador=0
        for i in range(1,num+1):
            if(num%i==0):
                contador+=1
        if(contador==2):
            print(str(num)+" es un numero primo")
        else:
            print(str(num)+" no es un numero primo")
        break
    


        
