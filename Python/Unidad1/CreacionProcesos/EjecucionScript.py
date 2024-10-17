import subprocess

result=subprocess.run(["python","CreacionProcesos/programa.py"], capture_output=True,text=True)

print(result.stdout)