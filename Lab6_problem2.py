#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Lab 6
#Problem 2

n = int(input("Enter a positive integer: "))+1
x=n-1
r=n
for i in range (1,n):
    for j in range (n-1,i,-1):
        print(".",end="")
    for b in range (1,i+1):
        val = i
        print(val,end="")
    print()
