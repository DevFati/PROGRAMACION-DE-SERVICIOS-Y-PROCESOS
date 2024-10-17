# Escriba un programa que simule un juego en el que dos jugadores (Alberto y
#Bárbara) tiran un dado. El que saque el valor más alto, gana. Si la puntuación
#coincide, empatan.


import random

print("JUEGO DE DADOS")
Alberto=random.randint(1,6)
Barbara=random.randint(1,6)
print("Alberto ha sacado "+str(Alberto))
print("Barbara ha sacado "+str(Barbara))
if Alberto == Barbara:
    print("Han empatado")
elif Alberto > Barbara:
   
    print("Alberto gana")
else:
 
    print("Barbara gana")
