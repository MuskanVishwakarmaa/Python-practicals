#Q5. Write a python program to Replace all spaces from text with – (dash).

def program5():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("MyFile.txt","r") as f1:
       data = f1.read()
       data=data.replace(' ','-')
    with open("MyFile.txt","w") as f1:
        f1.write(data)
program5()