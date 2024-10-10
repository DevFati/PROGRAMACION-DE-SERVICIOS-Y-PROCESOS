print("Hola Mundo")
valor=3
print(valor)

import keyword

print(keyword.kwlist) #Lista de palabras clave

print(keyword.iskeyword("paco"))

#comentarios 

help("modules") #Vr tdos los modulos 

edad,nombre=24, "Maria"
print("La edad de ",nombre,"es",edad)

print("Me dijo \"voy a ir\"") #Para poder imprimir comillas se pone brackets delante

semanas=4
print("En ",semanas,"semanas hay ",7*semanas,"dias")

print(f'¡Hola {nombre}!') #f hace que se puedan poner variables entre corchetes

#input 
nombre=input("¿Como te llamas?: ")
print("Hola",nombre)

print(2*3/5)
print(2/5*3)

print(divmod(13,4))  #da de resultado el cociente y el resto 
print(2**3)  #Potencia

n=2/5*3
print(round(4.5687647,3)) #Lo redondeara con 3 decimales. ara que acabe con .0 redondeado hay que poner 0 decimales
print(int(n)) #Truncar un numero

import math 

print(math.floor(n)) #Lo redondea hacia abajo
print(math.ceil(n)) #Lo redondea hacia arriba

print(abs(-5))

print(max(2,4,8)) #Coge el maximo del conjunto

print(min(4,9,7,1)) #Coge el minimo del conjunto
print(max("Ángela","Rocio","Pedro"))  

print(sorted((3,1,5,8,7,5)))

A=True

print(not A)

edad=67
print(edad>7)

if(edad>18 and edad <65):
    print("Es mayor de edad")
elif(edad>=65):
    print("Es jubilado")
else:
    print("Es menor de edad")


#Condicionales en una sola linea 
print("Es mayor de edad") if (edad>18) else print ("Es menor de edad")

#Funciones 

def division(x,y):
    q=x/y
    r=x%y
    return(q,r)

division(4,2)
print(division(x=4,y=2))