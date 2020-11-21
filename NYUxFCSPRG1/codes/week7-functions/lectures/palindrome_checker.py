def main():
    # ask for user input
    user_input = input("Please enter a sentence:\n")

    # sterilize sentence
    user_input = sterilize(user_input)

    # check if normal equals reversed
    verdict = "is a palindrome" if user_input == user_input[::-1] else "is not a palindrome"

    # render result
    print("Your sentence {}".format(verdict))

def sterilize(string):
    # define value to be removed
    forbidden = "!@#$%^&*()_-+={[}]|\\:;'<,>.?/ "

    for char in string:
        if char in forbidden:
            string = string.replace(char, "")
    
    # return lowercased string
    return string.lower()

main()