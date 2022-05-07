name = input("enter the name:")
age = int(input("enter the age:")) #by adding int at the front we are taking age as int instead of string
print("you entered your name as",name)
print("you entered your age as",age)
if int(age)>=0 and int(age)<=12:
    print("you are a child")
if int(age) >= 13 and int(age) <= 21:
    print("you are a teenager")
if int(age) >= 22 and int(age) <= 59:
    print("you are a man")
if int(age) >=60:
    print("you are an old man")
print("the data type of age is",type(age))    
print("the data type of name is",type(name))
a = float(age)
print("the data type of age after conversion is",type(a))