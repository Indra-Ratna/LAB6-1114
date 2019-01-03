#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Lab 6
#Problem 5
n =int(input("Enter a positive integer, n: "))
even = 0
odd = 0
j=0
for i in range (1,n):
    if i>10:
        if((i%10)%2==0):
            even+=1
        elif((i%10)%2!=0):
            odd+=1
        if(((i//10)%10)%2==0):
            even+=1
        elif(((i//10)%10)%2!=0):
            odd+=1
    elif i<10:
        if(i%2==0):
            even+=1
    else:
        odd+=1
    if(even>odd):
        print(i)
    even=0
    odd=0

"""
Lab Solution
n = int(input(...))
for i in range(1,n+1):
    even = 0
    odd = 0
    num = i
    while num>0:
        check = num % 10
        num//=10
        if check %2 == 0:
            even+=1
        else:
            odd+=1
    if(even>odd):
        print(i)
"""
 
