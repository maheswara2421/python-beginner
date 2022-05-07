print("please enter any number")
x = int(input("enter x value:"))
y = int(input("enter y value:"))
z = int(input("enter z value:"))
if x>y and x>z:
    print("your biggest number is:",x)
elif y>z:
    print("your biggest number is:",y)
else:
    print("your biggest number is:",z)