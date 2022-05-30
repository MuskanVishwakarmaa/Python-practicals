#Q1. Write a Python program to input a number, if it is not a number generates an error message.

while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
		
