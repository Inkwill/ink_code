import turtle
import math
import polygon
import flower

# def flower(tur, n, radius):
# 	angle = 120
# 	for x in range(n):
# 		polygon.arc(tur, radius, angle)
# 		tur.lt(180/n)

if __name__ == "__main__":
	tur1 = turtle.Turtle()
	tur2 = turtle.Turtle()

	flower.move(tur1,-100)
	flower.flower(tur1,10, 100, 80)

	flower.move(tur2, 100)
	flower.flower(tur2,10, 100, 60)
	turtle.mainloop()


