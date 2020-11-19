import turtle

print("Please enter the length of each side:")
side = float(input())

# rendering the square
for _ in range(4):
    turtle.forward(side)
    turtle.right(90)
turtle.hideturtle()
turtle.done()