#Q3. Count the total number of upper case, lower case, and digits used in the text file “MyFile.txt”.

def program3():
    with open("MyFile.txt","r") as f1:
       data=f1.read()
    cnt_ucase =0
    cnt_lcase=0
    cnt_digits=0
    for ch in data:
        if ch.islower():
            cnt_lcase+=1
        if ch.isupper():
            cnt_ucase+=1
        if ch.isdigit():
            cnt_digits+=1
    print("Total Number of Upper Case letters are:",cnt_ucase)
    print("Total Number of Lower Case letters are:",cnt_lcase)
    print("Total Number of  digits are:",cnt_digits)
program3()
