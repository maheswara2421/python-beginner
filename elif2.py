print("please enter a number between 0 to 256")
X = int(input("enter a number:"))
if X<0:
    print("your entered value is:",X)
    print("you entered a negative number")
    print("you entered an invalid number")
elif X==0:
    print("your entered value is:",X)
    print("you entered a neutral number")
    print("you entered an invalid number")
elif X<=256:
    print("your entered value is:",X)
    print(" you entered a positive number")
    print("you entered an valid number")
else:
    print("your entered value is:",X)
    print("you entered a positive number")
    print("you entered an invalid number")