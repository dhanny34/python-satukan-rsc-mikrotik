from cgi import test
from cgitb import text


data=open("datauser.txt").readlines()
datahasil = open('hasiluser.txt', 'w')
for n,line in enumerate(data):
    if line.startswith("add"):
       data[n] = "\n"+line.rstrip()
    else:
       data[n]=line.rstrip()

print (''.join(data), file=datahasil)
datahasil.close