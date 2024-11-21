import subprocess

result=subprocess.run(["python","RepasoExamen/sumatoria.py","5"],capture_output=True,text=True,check=False)

print(result.stdout)