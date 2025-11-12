#Program to check if user input numbers are equal without using any comparison operators
def checkifsame(n1,n2):
    if((n1^n2)!=0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")
n1=int(input("Enter the first number to compare"))
n2=int(input("Enter the second number to compare"))
checkifsame(n1,n2)