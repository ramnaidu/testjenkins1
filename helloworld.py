import subprocess
string = "hello world.. this is python file"
print(string)
ls = ["welcome","to","jenkins"]
for i in ls:
  print(i+" ")
print("pytest version is:")
proc = subprocess.run('pytest --version',shell=True,stdout=subprocess.PIPE)
print(proc.stdout.decode("utf-8"))
