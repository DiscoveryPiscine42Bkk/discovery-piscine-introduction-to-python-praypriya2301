
import sys

if len(sys.argv) == 2:
    parameter = sys.argv[1]
    user_input = input("What was the paraneter? ")

    if user_input == parameter :
        print("Good jod!")
    else:
        print("Nope, sorry...")
else:
    print("none")