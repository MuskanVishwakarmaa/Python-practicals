#Q7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d={"Upper_Case":0, "Lower_Case":0}
    for c in s:
        if c.isupper():
           d["Upper_Case"]+=1
        elif c.islower():
           d["Lower_Case"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["Upper_Case"])
    print ("No. of Lower case Characters : ", d["Lower_Case"])

string_test('The quick brown fox jumps over the lazy dog')
