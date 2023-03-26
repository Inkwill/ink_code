'''ex5.1 
The time module provides a function, also named time, 
that returns the current Greenwich Mean Time in "the epoch", 
which is an arbitrary time used as a reference point. 
On UNIX systems ,the epoch is 1 January 1970.'''


import time
import turtle

def curTime(time):
	days = time//(3600*24)
	hours = (time - 3600*24*days)//3600
	minutes = (time - 3600*24*days - 3600*hours)//60
	seconds = (time - 3600*24*days - 3600*hours)%60
	print("{0}days-{1}h-{2}m-{3}s".format(int(days),int(hours)+8,int(minutes),int(seconds)))

# curTime(time.time())

'''ex5.2
Fermat's Last Theorem says that there are no popsitive integers a,b, and c such that a^n + b^n = c^n
for any values of n greater than 2.
Write a function named check_fermat that takes four parameters- a,b,c and n- and checks to see if Fermat's theorem holds. if n is greater than 2 
and  the program should print "Holy smokes, Fermat was wrong!" Otherwise the program should print, "No, that doesn't work."
'''

def check_fermat(a, b,c,n):
	a = input("Input a:")
	b = input("Input b:")
	c = input("Input c:")
	n = input("Input n:")
	if a**n + b**n == c**n:
		print("Holy smokes, Femat was wrong!")
	else:
		print("No,that doesn't work.")


''' ex5.4'''
def recurse(n, s):
	''' sum s to zero'''
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)
# recurse(3, 0)


'''ex5.5'''
def draw(t, length, n):
	if n==0:
		return
	angle = 30
	t.fd(length*n)
	t.lt(angle)
	draw(t,length,n-1)
	t.rt(2*angle)
	draw(t,length,n-1)
	t.lt(angle)
	t.bk(length*n)

# t = turtle.Turtle()
# draw(t, 10, 6)

'''ex5.6
To draw a Koch cruve with length x, all you have to do is:
1. Draw a Koch curve with length x/3
2. Turn left 60 degrees
3. Draw a Koch cruve with length x/3
4. Turn right 120 degrees
5. Draw a Koch cruve with length x/3
6 Turn left 60 degrees.
7. Draw a Koch curve with length x/3
8. The exception is if x is less than 3: in that case, you can just draw a straight line with length x.
'''
def draw_koch(t, length):
	if length < 9:
		t.fd(length)
	else:
		draw_koch(t,length/3)
		t.lt(60)
		draw_koch(t,length/3)
		t.rt(120)
		draw_koch(t,length/3)
		t.lt(60)
		draw_koch(t,length/3)

def snowflake(t,length):
	draw_koch(t,length)
	t.rt(120)
	draw_koch(t,length)
	t.rt(120)
	draw_koch(t,length)

t = turtle.Turtle()
snowflake(t,100)
turtle.mainloop()

