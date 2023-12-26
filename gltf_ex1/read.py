from struct import unpack
import numpy

f=open('test.bin','rb')
x1=f.read(312)
x2=f.read(312)
x3=f.read(208)
x4=f.read(72)
f.close()

d1=unpack('<'+'f'*(len(x1)//4),x1)
n1=numpy.array(d1)
r1=numpy.reshape(n1,(int(len(n1)/3),3))
d2=unpack('<'+'f'*(len(x2)//4),x2)
n2=numpy.array(d2)
r2=numpy.reshape(n2,(int(len(n2)/3),3))
for i in range(0,len(r1)):
    print(i,r1[i],r2[i])
#print('r1',len(r1),r1)
#print('r2',len(r2),r2)
d3=unpack('<'+'f'*(len(x3)//4),x3)
n3=numpy.array(d3)
r3=numpy.reshape(n3,(int(len(n3)/2),2))
print('r3',len(r3),r3)
s4=unpack('<'+'h'*(len(x4)//2),x4)
n4=numpy.array(s4)
r4=numpy.reshape(n4,(int(len(n4)/3),3))
print('r4',len(r4),r4)

