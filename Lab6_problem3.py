#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Lab 6
#Problem 3

n = int(input("Enter a positive integer: "))
for i in range(0,n):
    for k in range(1,i+1):
        print("#",end="")
    print("%",end="")
    for b in range(n-1,i,-1):
        print("$",end="")
    print()
