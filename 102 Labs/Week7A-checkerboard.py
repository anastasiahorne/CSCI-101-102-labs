#Anastasia Horne
#CSCI 102 – Section G
#Week 7 - Lab A - Checkerboard
#References: Video Help for checkerboard lab
#Time: 30 minutes

n=int(input('LENGTH>'))
first= input('FIRST>')
second= input('SECOND>')

small=[]
big=[]
for i in range(n):
    if i%2==0:
        for i in range(n):
            if i%2==0:
                small.append(first)
            else:
                small.append(second)
    else:
        for i in range(n):
            if i%2==0:
                small.append(second)
            else:
                small.append(first)

    big.append(small)
    small=[]
for i in range(n):
    print('OUTPUT',big[i])
    
print('OUTPUT',big)
