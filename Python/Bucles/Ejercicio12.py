#Escriba un programa que pida un nu mero entero mayor que cero y calcule su factorial.
salir=True
while (salir):
    m=int(input("Introduce un numero entero mayor que 0: "))

    if(m>0):
        resultado=1
        for i in range(1,m+1):
            resultado=resultado*i
        print("El factorial de "+str(m)+" es: "+str(resultado))
        salir=False
