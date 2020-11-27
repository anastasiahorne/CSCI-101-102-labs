#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 10
#References: None
#Time: 80 minutes


#words from dictionary to a list
words= open('dictionary.txt','r')
word_str=words.read()
word_list= word_str.split('\n')
words.close()


#amount with same length as inputted
length=int(input('LENGTH>'))
same_length=0
sl_list=[]
for i in range(0,len(word_list)):
    if len(word_list[i])==length:
        same_length+=1
        sl_list.append(word_list[i])
    else:
        continue
print('OUTPUT',same_length)



#how to get the random word

import random
lo_list= len(sl_list)
my_seed= int(input('SEED>'))
random.seed(my_seed)
index=random.randint(0,lo_list)
random_word= sl_list[index]
print('OUTPUT',random_word)


#how to get longest word(s) from entire dictionary

length_list=[]
for i in range(0,len(word_list)):
    length_word= len(word_list[i])
    length_list.append(length_word)
max_length= max(length_list)
index_list=[]
for i in range(0,len(length_list)):
    if length_list[i]==max_length:
        index_list.append(i)
    else:
        continue
lw_list=[]
for i in range(0,len(index_list)):
    index= index_list[i]
    lw_list.append(word_list[index])
print('OUTPUT',lw_list)
        
        


