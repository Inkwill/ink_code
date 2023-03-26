import turtle
import polygon
import math


def draw_spiral(t, n, length=10,a=0.01,b=0.0002):
	theta = 0.0

	for i in range(n):
		t.fd(length)
		dtheta = 1/ (a+b*theta)

		t.lt(dtheta)
		theta += dtheta

if __name__ == "__main__":
	t = turtle.Turtle()
	draw_spiral(t,n=1000)

	turtle.mainloop()
