# import libraries
import turtle

def main():
    # draw_single will render a single square
    def draw_single(step):
        for _ in range(4):
            turtle.forward(step)
            turtle.left(90)

    # draw function will render all of the squares
    def draw(num=6, step=100):
        turn_angle = int(360 / num)
        for _ in range(num):
            draw_single(step)
            turtle.left(turn_angle)
        turtle.hideturtle()
        turtle.done()


    print("Please enter number of squares: ")
    user_input = int(input())

    # function to render the expected result
    draw(user_input)

# initiate the program
main()