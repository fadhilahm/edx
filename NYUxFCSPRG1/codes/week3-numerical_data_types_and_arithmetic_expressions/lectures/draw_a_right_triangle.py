import turtle, math

print("Enter the length of the two legs in a right triangle")
legs = []
angles = [90]
for i in range(2):
    legs.append(float(input("Leg #{}: ".format(i + 1))))
legs.append((legs[0] ** 2 + legs[1] ** 2) ** 0.5)
angles.append(math.degrees(math.atan(legs[0] / legs[1])))
angles.append(90 - angles[1])

# render the triangle
for i in range(len(legs)):
    turtle.forward(legs[i])
    angle = angles[i] if i == 0 else 180 - angles[i]
    turtle.left(angle)
turtle.hideturtle()
turtle.done()    
        