#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 9
#References: None
#Time: 80 minutes

Upper_Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lower_Alphabet='abcdefghijklmnopqrstuvwxyz'
string= input('STRING>')
index=0
old=''
new=''
new_index=0
string_list=[]

for i in range(0,len(string)):
    string_list.append(string[i])


for i in range(0,len(string_list)):
    if string_list[i] in Upper_Alphabet:
        index= Upper_Alphabet.find(string_list[i])
        new_index=25-index
        new=Upper_Alphabet[new_index]
        string_list[i]=new
    elif string_list[i] in Lower_Alphabet:
        index= Lower_Alphabet.find(string_list[i])
        new_index=25-index
        new=Lower_Alphabet[new_index]
        string_list[i]=new
    else:
        continue
delimeter=''
encrypted_string=delimeter.join(string_list)
print(f'Your Atbash cipher is: {encrypted_string}')
print('OUTPUT',encrypted_string)
