import turtle
turtle.Screen().bgcolor("yellow")
sc=turtle.Screen()
sc.setup(400,300)

turtle.title("welocme to turtle square")

board=turtle.Turtle()

for i in range(4):
  board.forward(80)
  board.right(90)
  i=i+1

turtle.done()