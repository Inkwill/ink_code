import polygon as pl
import turtle
import math

def triangle(t,length,angle):
	"""Draw a equicrural triangle
	t: trutle
	length: length of a crural
	angle: apex angle (degrees) """

	angle = 90 + angle/2
	side = abs(length * math.cos(angle * math.pi/180))*2
	t.fd(length)
	t.lt(angle)
	t.fd(side)
	t.lt(angle)
	t.fd(length)

def pie(t,length,n):
	"""Draw a pie by triangle
	t: trutle
	length:length of pie
	n:number of triangle """
	tur.rt(180/n)
	for i in range(n):
		triangle(t,length,360/n)
		t.lt(180)

tur = turtle.Turtle()
pie(tur,100,20)
#pl.polygon(tur,6,100)
#tur.lt((180 - 360/6)/2)
#tur.fd(abs(100/2/math.cos((math.pi - 2*math.pi/6)/2)))
turtle.mainloop()
