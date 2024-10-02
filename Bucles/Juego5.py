#Escriba un programa que pida un número de dados, que tire el número de dados
#indicado y diga cuál es el valor más alto obtenido.
import random
salir=True
resultados=list()
while(salir):
    print("EL DADO MÁS ALTO(1)")
    m=int(input("Número de dados: "))
    if(m<=0):
        print("¡Imposible!")
    else:
        for i in range (0,m):
            resultados.append(random.randint(1,6))
        print("Dados:",*resultados, sep=" ")
        
        #el parametro sep lo que hace es separar los elementos en este caso con un espacio 
        #cuando se imprimen. Su formato es el de arriba. Obligatorio que los diferentes 
        #parametros esten separados por comas para que funcione. "texto",*lista,sep " "

        print("El dado más alto es: "+str(max(resultados)))
        salir=False




   
  