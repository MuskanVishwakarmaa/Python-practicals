#Q2. Create a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input statements from the user.

def program2():
    f = open("MyFile.txt","w")
    line1=input("Enter the text:")
    line2=input("Enter the text:")
    line3=input("Enter the text:")
    new_line="\n"
    f.write(line1)
    f.write(new_line)
    f.write(line2)
    f.write(new_line)
    f.write(line3)
    f.write(new_line)
    f.close()
program2()