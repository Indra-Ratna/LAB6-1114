#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Lab 6
#Problem 4
n = int(input("Enter a positive integer,n: "))
s = int(input("Enter a starting value: "))
for i in range (n,n+s):
    for b in range (n,i+1):
        print(i,end="")
    print()
for i in range (n+s-1,n-1,-1):
    for b in range (i,n,-1):
        print(i,end="")
    print()
