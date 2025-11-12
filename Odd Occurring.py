#Program to find the element not making a pair
#Function to calculate the number that is odd occurring
def oddoccurring(arr):
    #initialize result
    res=0
    for element in arr:
        res=res^element
    return res
arr=[]
n=int(input("Enter the array size"))
while n:
    num=int(input("Enter number"))
    arr.append(num)
    n-=1
print("Odd occurning number is:",oddoccurring(arr))