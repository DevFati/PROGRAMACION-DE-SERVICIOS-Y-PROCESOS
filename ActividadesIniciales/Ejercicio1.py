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
