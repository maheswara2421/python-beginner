A = [10,2,4,50,49,64,89,76,54,2]
Y = bytes(A)
print(type(Y))
print(type(A))
print(Y[0])
print(Y[1])
print(Y[3])
print(Y[4])
print(Y[5])
for a in Y:
    print(A)    #here capital "a" displays all numbers multiple(no of elements in the list) times vertical  line
for a in Y:
    print(a)   #here small "a" displays all numbers once in horizontal line