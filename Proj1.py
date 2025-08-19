a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))


print("Enter 1 for 'Addiction' \nEnter 2 for 'Subtraction'\nEnter 3 for 'Multiplication' \nEnter 4 for 'Division' ")

Enter_num = int(input("Choose a num form 1 - 4: "))

if Enter_num == 1:
    print("The answer of ", a ,"+", b ,"is :", a + b)
elif Enter_num == 2:
    print("The answer of ", a ,"-", b ,"is :", a - b)
elif Enter_num == 3:
    print("The answer of ", a ,"*", b ,"is :", a * b)
elif Enter_num == 4:
    print("The answer of ", a ,"/", b ,"is :", a / b)
else:
    print("Select a valid  option.")
#print("The answer of ", a ,"**", b ,"is :", a ** b)
#print("The answer of ", a ,"//", b ,"is :", a // b)
