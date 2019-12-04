from subprocess import run,PIPE
out = run(['python','go.py'],stdout=PIPE)
print (type(out.stdout))
s=bytes.decode(out.stdout)
print(s)
