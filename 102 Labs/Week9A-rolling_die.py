#Anastasia Horne
#CSCI 102 – Section G
#Week 9 - Lab A - Rolling a Die
#References: None
#Time:15 minutes

num_rolls= int(input('NUMBER>'))
num_seed= int(input('SEED>'))
roll_num=''
import random
random.seed(num_seed)
for i in range(0,num_rolls):
    roll_num +=str(random.randint(1,6))

for i in range(1,7):
    print('OUTPUT',i,'occured',roll_num.count(str(i)),'times')
