import subprocess

result=subprocess.run(["python","CreacionProcesos/Suma.py","4","7"],capture_output=True,text=True,check=False)

print(result.stdout)