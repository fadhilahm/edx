grade_input = float(input("Please enter a grade: "))
letter = None

if 90 <= grade_input <= 100:
    letter = "A"
elif 80 <= grade_input <= 89:
    letter = "B"
elif 70 <= grade_input <= 79:
    letter = "C"
elif 60 <= grade_input <= 69:
    letter = "D"
elif 0 <= grade_input <= 59:
    letter = "F"

if letter:
    print(letter)
else:
    print("Invalid Grade")