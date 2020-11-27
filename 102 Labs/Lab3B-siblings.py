#Anastasia Horne
#CSCI 102 – Section G
#Week 3 - Lab B - Three Siblings
#References: no one
#Time: 40 minutes
number= int(input('NUMBER>'))
print(f'The sibling(s) who will work with {number} follow:')
if (number%2) != 0:
    print('OUTPUT Jimmy')
if (number>=10) and (number<=100):
    print('OUTPUT Jared')
number=str(number)
if (len(number)==2) and ((int(number[0]) + int(number[1]))==6) or ((int(number[0])+ int(number[1]))==8):
    print('OUTPUT Josephine')




