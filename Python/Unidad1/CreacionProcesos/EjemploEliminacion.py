import psutil 
import time 

for proc in psutil.process_iter():
    try: 
        #El notepad tiene que estar abierto 
        #Obtener el nombre del proceso 
        nombreProceso=proc.name()
        if proc.name() == "notepad.exe":
            PID=proc.pid
            time.sleep(5)
            print("Eliminando el proceso: ", nombreProceso, ' ::: ',PID)
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("error")