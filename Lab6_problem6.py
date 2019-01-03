#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Lab 6
#Problem 6
#lab sol
print("Enter a sequence of positive integers, each one on a separate line.")
print("End your sequence by typing -1: ")
isEnd = False
mono=0
while(not isEnd):
    val = int(input())
    if val == -1:
        isEnd = True
    else:
        isMono=True
        mono=val%10
        while(val>0 and isMono):
            digit = val%10
            val//=10
            if digit!=mono:
                isMono = False
        if isMono:
            mono +=1
print(mono)

isEnd = False
mono = 0
while(not 
