import turtle
import flower
import math
import polygon

def draw_line(t,startpos,endpos):
	"""Draws a line from startpos to endpos.
	startpos: start point
	endpos: end point
	"""
	pos = t.pos()
	t.pu()
	t.goto(startpos[0],startpos[1])
	t.pd()
	t.goto(endpos[0],endpos[1])
	t.pu()
	t.goto(pos[0],pos[1])
	t.pd()

def polyline(t, n, length, angle, dir='left'):
	"""Draws n line segments.
	t: Turtle object
	n: number of line segments
	length: length of each segment
	angle: degrees between segments
	dir : direction,'right' or 'left'
	"""
	for i in range(n):
		t.fd(length)
		if dir.lower() == 'right':
			t.rt(angle)
		elif dir.lower() == 'left':
			t.lt(angle)

def arc(t, r, angle,dir):
	"""Draws an arc with the given radius and angle.

	t: Turtle
	r: radius
	angle: angle subtended by the arc, in degrees
	"""
	arc_length = 2 * math.pi * r * abs(angle) / 360
	n = int(arc_length / 4) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n

	# making a slight left turn before starting reduces
	# the error caused by the linear approximation of the arc
	if dir == 'left':
		t.lt(step_angle/2)
		polyline(t, n, step_length, step_angle,dir)
		t.rt(step_angle/2)
	else:
		t.rt(step_angle/2)
		polyline(t, n, step_length, step_angle,dir)
		t.lt(step_angle/2)

def center_arc(t,r,startangle, endangle,dir):
	startangle = startangle if startangle >0 else 360 + startangle
	endangle = endangle if endangle >0 else 360 + endangle

	if startangle > endangle:
		angle = startangle - endangle if dir == 'right' else 360 - startangle + endangle
	else:
		angle = endangle - startangle if dir == 'left' else 360 + startangle - endangle

	t.pu()
	t.lt(startangle)
	t.fd(r)
	t.pd()
	if dir == 'right':
		t.rt(90)
	else:
		t.lt(90)
	arc(t,r,angle,dir)
	t.setheading(0)

def draw_arc(t,startpos,endpos,centerdis,dir):
	pos = t.pos()
	centerpos =[0,0]
	centerO = [0,0]
	s = math.sqrt((endpos[1]-startpos[1])**2+(endpos[0]-startpos[0])**2)
	print("s={0}".format(s))
	if endpos[1] == startpos[1]:
		centerpos[0] = (endpos[0]-startpos[0])/2+startpos[0]
		centerpos[1] = centerdis + startpos[1]
	elif endpos[0] == startpos[0]:
		centerpos[0] = centerdis + startpos[0]
		centerpos[1] = (endpos[1]-startpos[1])/2+startpos[1]
	else:
		centerO[0] = (endpos[0]+startpos[0])/2
		centerO[1] = (endpos[1]+startpos[1])/2

		k = abs(endpos[0]-startpos[0])/abs(endpos[1]-startpos[1])
		b = centerO[1] - k*centerO[0]

		if centerdis == 0:
			centerpos = centerO
		else:
			t.pu()
			t.goto(centerO[0],centerO[1])
			t.lt(math.atan(k)*180/math.pi)
			t.fd(centerdis)
			t.rt(math.atan(k)*180/math.pi)
			centerpos = t.pos()
			# l1 = abs(k*startpos[1]+b-startpos[1])
			# p = l1**2 - (s *0.5)**2
			# l2 = math.sqrt(p)
			# print((l2*s/2 - centerdis*s/2)/l1)
			# centerpos[0] = startpos[0] + (l2*s/2 - centerdis*s/2)/l1
			# centerpos[1] = k*centerpos[0] + b
	print('start:{0}'.format(startpos))
	print('end:{0}'.format(endpos))
	print('center:{0}'.format(centerpos))

	r = math.sqrt((startpos[0]-centerpos[0])**2+(startpos[1]-centerpos[1])**2)

	def getangle(p1,p2):
		if p1[1] == p2[1]:
			return 0 if p2[0] > p1[0] else 180
		elif p1[0] == p2[0]:
			return 90 if p2[1] > p1[1] else 270
		else:
			tan = (p2[1]-p1[1])/(p2[0]-p1[0])
			return math.atan(tan)*180/math.pi if p2[0] > p1[0] else 180 + math.atan(tan)*180/math.pi

	startangle = getangle(centerpos, startpos)
	endangle = getangle(centerpos, endpos)
	print(startangle,endangle)
	
	#draw_line(t, centerpos, startpos)
	#draw_line(t, centerpos, endpos)
	t.pu()
	t.goto(centerpos[0],centerpos[1])
	t.pd()
	center_arc(t,r,startangle,endangle,dir)
	t.pu()
	t.goto(pos[0],pos[1])
	t.pd()

def move(t,length,angle):
	t.lt(angle)
	t.pu()
	t.fd(length)
	t.pd()
	t.rt(angle)

def moveto(t,pos):
	t.pu()
	t.goto(pos[0],pos[1])
	t.pd()


def draw_a(t,size):
	x = t.pos()[0]
	y = t.pos()[1]

	draw_line(t,(x,y+size*0.5),(x-size*0.5,y-size*0.5))
	draw_line(t,(x,y+size*0.5),(x+size*0.5,y-size*0.5))
	draw_line(t,(x-size*0.25,y),(x+size*0.25,y))
	

def draw_b(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y)
	c = (x-size*0.25,y-size*0.5)
	draw_line(t,a,c)
	draw_arc(t,a,b,size*0.15,'right')
	draw_arc(t,b,c,size*0.15,'right')

def draw_c(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x+size*0.4,y+size*0.4)
	b = (x+size*0.4,y-size*0.4)
	draw_arc(t,a,b,-size*0.25,'left')

def draw_d(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.4,y+size*0.4)
	b = (x-size*0.4,y-size*0.4)
	draw_line(t,a,b)
	draw_arc(t,a,b,size*0.25,'right')

def draw_e(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y)
	c = (x-size*0.25,y-size*0.5)
	draw_line(t,a,c)
	draw_line(t,a,(x+size*0.25,y+size*0.5))
	draw_line(t,b,(x+size*0.25,y))
	draw_line(t,c,(x+size*0.25,y-size*0.5))

def draw_f(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y)
	c = (x-size*0.25,y-size*0.5)
	draw_line(t,a,c)
	draw_line(t,a,(x+size*0.25,y+size*0.5))
	draw_line(t,b,(x+size*0.25,y))

def draw_g(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x+size*0.4,y+size*0.2)
	b = (x+size*0.4,y-size*0.1)
	draw_arc(t,a,b,-size*0.4,'left')
	draw_line(t,(x+size*0.4-10,y-size*0.1),(x+size*0.4+10,y-size*0.1))

def draw_h(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a1 = (x-size*0.25,y+size*0.5)
	b1 = (x-size*0.25,y)
	c1 = (x-size*0.25,y-size*0.5)
	a2 = (x+size*0.25,y+size*0.5)
	b2 = (x+size*0.25,y)
	c2 = (x+size*0.25,y-size*0.5)
	draw_line(t,a1,c1)
	draw_line(t,a2,c2)
	draw_line(t,b1,b2)

def draw_i(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a1 = (x-size*0.25,y+size*0.5)
	b1 = (x-size*0.25,y-size*0.5)
	a2 = (x,y+size*0.5)
	b2 = (x,y-size*0.5)
	a3 = (x+size*0.25,y+size*0.5)
	b3 = (x+size*0.25,y-size*0.5)
	draw_line(t,a1,a3)
	draw_line(t,a2,b2)
	draw_line(t,b1,b3)

def draw_j(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.4,y+size*0.5)
	b = (x+size*0.4,y+size*0.5)
	c = (x,y+size*0.5)
	d = (x,y-size*0.3)
	f = (x-size*0.5,y-size*0.3)
	draw_line(t,a,b)
	draw_line(t,c,d)
	draw_arc(t,d,f,0,'right')

def draw_k(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y-size*0.5)
	c = (x-size*0.25,y)
	d = (x+size*0.5,y+size*0.5)
	e = (x+size*0.5,y-size*0.5)
	draw_line(t,a,b)
	draw_line(t,c,d)
	draw_line(t,c,e)

def draw_l(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y-size*0.5)
	c = (x+size*0.4,y-size*0.5)
	draw_line(t,a,b)
	draw_line(t,b,c)

def draw_m(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y-size*0.5)
	b = (x-size*0.25,y+size*0.5)
	c = (x,y-size*0.25)
	d = (x+size*0.25,y+size*0.5)
	e = (x+size*0.5,y-size*0.5)
	draw_line(t,b,a)
	draw_line(t,b,c)
	draw_line(t,d,c)
	draw_line(t,d,e)

def draw_n(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y-size*0.5)
	b = (x-size*0.25,y+size*0.5)
	c = (x+size*0.25,y-size*0.5)
	d = (x+size*0.5,y+size*0.5)
	draw_line(t,b,a)
	draw_line(t,b,c)
	draw_line(t,d,c)

def draw_o(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	center_arc(t,size*0.5,0,360,'right')

def draw_p(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y)
	c = (x-size*0.25,y-size*0.5)
	draw_line(t,a,c)
	draw_arc(t,a,b,5,'right')

def draw_q(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	center_arc(t,size*0.5,0,360,'right')
	draw_line(t,(x,y),(x+size*0.5,y-size*0.5))

def draw_r(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.25,y+size*0.5)
	b = (x-size*0.25,y)
	c = (x-size*0.25,y-size*0.5)
	draw_line(t,a,c)
	draw_arc(t,a,b,5,'right')
	draw_line(t,b,(x+size*0.25,y-size*0.5))

def draw_s(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x+size*0.25,y+size*0.5)
	b = (x,y)
	c = (x-size*0.25,y-size*0.5)
	draw_arc(t,a,b,0,'left')
	draw_arc(t,b,c,0,'right')

def draw_t(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.4,y+size*0.5)
	b = (x+size*0.4,y+size*0.5)
	c = (x,y+size*0.5)
	d = (x,y-size*0.5)
	draw_line(t,a,b)
	draw_line(t,c,d)

def draw_u(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.4,y+size*0.5)
	b = (x-size*0.4,y-size*0.25)
	c = (x+size*0.4,y+size*0.5)
	d = (x+size*0.4,y-size*0.25)
	draw_line(t,a,b)
	draw_line(t,c,d)
	draw_arc(t,d,b,0,'right')

def draw_v(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y+size*0.5)
	b = (x,y-size*0.5)
	c = (x+size*0.5,y+size*0.5)
	draw_line(t,a,b)
	draw_line(t,c,b)

def draw_w(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y+size*0.5)
	b = (x-size*0.25,y-size*0.5)
	c = (x,y)
	d = (x+size*0.25,y-size*0.5)
	e = (x+size*0.5,y+size*0.5)

	draw_line(t,a,b)
	draw_line(t,b,c)
	draw_line(t,c,d)
	draw_line(t,d,e)

def draw_x(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y+size*0.5)
	b = (x+size*0.5,y+size*0.5)
	c = (x-size*0.5,y-size*0.5)
	d = (x+size*0.5,y-size*0.5)

	draw_line(t,a,d)
	draw_line(t,b,c)

def draw_y(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y+size*0.5)
	b = (x+size*0.5,y+size*0.5)
	c = (x,y)
	d = (x,y-size*0.5)
	draw_line(t,a,c)
	draw_line(t,b,c)
	draw_line(t,c,d)

def draw_z(t,size):
	x = t.pos()[0]
	y = t.pos()[1]
	a = (x-size*0.5,y+size*0.5)
	b = (x+size*0.5,y+size*0.5)
	c = (x-size*0.5,y-size*0.5)
	d = (x+size*0.5,y-size*0.5)
	draw_line(t,a,b)
	draw_line(t,b,c)
	draw_line(t,c,d)

if __name__ == "__main__":
	t = turtle.Turtle()
	#draw_a(t)
	#draw_arc(t,(0,0),(0,200),90)
	draw_c(t,100)
	t.hideturtle()
	turtle.mainloop()
