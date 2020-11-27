#Anastasia Horne
#CSCI 101 – Section A
#Python Lab 6
#References: None
#Time: 190 minutes

DNA_str= input('DNASTRING>')
i=0
b=0

number_A=0
number_C=0
number_G=0
number_T=0
DNA_allowed=['A','C','G','T']
check=True

for i in range(0,len(DNA_str)):    
    A=DNA_str[i]             
    if A is 'A':
        number_A= number_A+1
    elif A is 'C':
        number_C= number_C+1
    elif A is 'G':
        number_G= number_G+1
    elif A is 'T':
        number_T= number_T+1        
    else:
        print('OUTPUT DNA string not valid')
        check=False
        break
RNA_str=''
if check:
    print('OUTPUT',number_A,number_C,number_G,number_T)
    for b in range(0,len(DNA_str)):
        A=DNA_str[b]
        if A is 'T':
            RNA_str= RNA_str + 'U'
        else:
            RNA_str= RNA_str + A
    print('OUTPUT',RNA_str)
    





