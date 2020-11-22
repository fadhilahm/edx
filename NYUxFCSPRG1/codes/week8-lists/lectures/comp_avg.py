def main():
    # introductory message
    print("Enter grades in separate lines.\nTo end the input type 'done':")

    # define list used to store student's grade and user_input
    students = []

    while True:
        user_input = input()
        if user_input == 'done':
            break
        else:
            students.append(int(user_input))

    # calculate avg
    avg = sum(students) / len(students)
    over_avg = list(filter(lambda x: x > avg, students))
    over_avg_s = ', '.join(str(num) for num in over_avg)

    # render output
    print(
"""The class average is {:.2f}
The grades above the average are {}""".format(avg, over_avg_s)
    )

main()
