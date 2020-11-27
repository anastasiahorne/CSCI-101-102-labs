#Anastasia Horne
#CSCI 102 – Section G
#Week 6 - Lab A - Visitors
#References: None
#Time:  120 minutes
print('When inputting names, sepaerate each by a space and comma, and the string should end with a comma')
user_str= input('USERS>')
user_list=[]
index_og=0
index_end=0


i=0
b=user_str[index_end]

while i<len(user_str):
    
    if user_str[i] == ',':
        Name=''
        name=Name+user_str[index_og:i]
        name=name.lower()
        user_list.append(name)
        index_og=i+2
    i+=1
print('OUTPUT',user_list)

name_number=0

print('OUTPUT', end='')
for x in range(0,len(user_list)):
    name_number= user_list.count(user_list[x])
    print(f' {user_list[x]}, {name_number},',end='')

    
    
    
    
