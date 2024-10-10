#while 

i=1
while i<=10:
    print(i)
    i+=1


#break 

fib_ant=1
fib=1
idx=3

print(f"El termino {fib_ant} ocupa la posicion 1")
print(f"El termino {fib} ocupa la posicion 2")


while fib<500000:
    temporal=fib
    fib=fib+fib_ant
    fib_ant=temporal 
    print(f"El termino {fib} ocupa la posicion {idx}")


    if idx ==20:
        break
    idx+=1

#while...else 

i=3
while i>=0:
    print(i)
    i-=1
else:
    print("Ha finalizado la cuenta atrás")

#for 

s=(1,2,4,5)

for c in s: 
    print(c)

#range(start,stop,step)

for i in range(10,0,-1):
    print(i)

#continue 

for i in range (101):
    if i%2==0 or i%5==0:
        continue 

    print(i)


for i in range(1,11):
    print(f"Tabla de multiplicar del {1}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")