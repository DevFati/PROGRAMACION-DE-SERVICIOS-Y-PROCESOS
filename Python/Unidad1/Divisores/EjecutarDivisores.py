import subprocess

result=subprocess.run(["python","Divisores.py","4"],capture_output=True,text=True,check=False)

print(result.stdout)