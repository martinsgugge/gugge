import math

x=10
y=10

angle=math.atan(y/x)

#print((angle/math.pi)*180) #må huske at trigonometriske funksjoner jobber med radianer

real=12.896
integer=42
string="Some String"

print('real={0:9.2f},integer={1},string={2}'.format(real,integer,string))
print('real={0},integer={1},string={2}'.format(format(real,'.3f'),integer,string))