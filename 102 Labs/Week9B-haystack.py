#Anastasia Horne
#CSCI 102 – Section G
#Week 9 - Lab B - Combing Through a Haystack
#References: No one 
#Time:  60 minutes

s_str= input('s>')
t_str= input('t>')
occurences=0

for i in range(0,len(s_str)):
    outer= i+len(t_str)
    compare=s_str[i:(outer)]
    if compare == t_str:
        occurences+=1
    else:
        continue

print('OUTPUT',occurences)
location=0
x=0
print('OUTPUT',end=' ')
for i in range(0,len(s_str),2):
    location= s_str.find(t_str,location+1)
    print(location+1, end=' ')
    x+=1
    if x==occurences:
        break
    else:
        continue
    
