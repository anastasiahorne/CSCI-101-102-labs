#Anastasia Horne
#CSCI 101 – Section A
#Python Lab 5
#References: Kevin Shin (Section F)
#Time:  240 minutes
binary_allowed= ['0','1']
octal_allowed= ['0','1','2','3','4','5','6','7']
decimal_allowed= ['0','1','2','3','4','5','6','7','8','9']
repeat='y'
while repeat== 'y' or repeat=='yes':
    option_number= int(input('OPTION>'))

    if option_number==1:
        check=True
        binary_given= input('BINARY_STR>')
        for f in range(0,len(binary_given)):
            x= binary_given[f]
            if x not in binary_allowed:
                check=False
        
 
        if check: 
            i=0
            result=0
            k= -1
            decimal_number=0
            
            while i<len(binary_given):       
                result= 2**(i) * int(binary_given[k])
                decimal_number= decimal_number + result
                i= i+1
                k= k-1
            print('OUTPUT',decimal_number)
        else:
             print(f'ERROR: {binary_given} is NOT a binary number')
   
    elif option_number==2:
        decimal_given= input('DECIMAL_STR>')
        check=True
        for f in range(0,len(decimal_given)):
            x= decimal_given[f]
            if x not in decimal_allowed:
                check=False


        if check:
            binary_str=[]
            a=0
            decimal_given= int(decimal_given)
            while decimal_given>0:
                a=decimal_given%2
                binary_str.append(a)
                decimal_given= decimal_given//2
            list_str= ''
            for f in range(len(binary_str)-1,-1,-1):
                list_str= list_str + str(binary_str[f])
            print('OUTPUT',list_str)
        else:
            print(f'ERROR: {decimal_given} is NOT a decimal number')


    elif option_number==3:
        check=True
        octal_given= input('OCTAL_STR>')
        for f in range(0,len(octal_given)):
            x= octal_given[f]
            if x not in octal_allowed:
                check=False
        
 
        if check: 
            i=0
            result=0
            k= -1
            decimal_number=0
            
            while i<len(octal_given):       
                result= 8**(i) * int(octal_given[k])
                decimal_number= decimal_number + result
                i= i+1
                k= k-1
            print('OUTPUT',decimal_number)
        else:
             print(f'ERROR: {octal_given} is NOT an octal number')
    elif option_number==4:
        decimal_given= input('DECIMAL_STR>')
        check=True
        for f in range(0,len(decimal_given)):
            x= decimal_given[f]
            if x not in decimal_allowed:
                check=False


        if check:
            octal_str=[]
            a=0
            decimal_given= int(decimal_given)
            while decimal_given>0:
                a=decimal_given%8
                octal_str.append(a)
                decimal_given= decimal_given//8
            list_str= ''
            for f in range(len(octal_str)-1,-1,-1):
                list_str= list_str + str(octal_str[f])
            print('OUTPUT',list_str)
        else:
            print(f'ERROR: {decimal_given} is NOT a decimal number')
    elif option_number==5:
        break
    else:
        print('ERROR: Please choose from [1-5]')
        continue

        
        


    repeat=input('CONTINUE>')
    repeat=repeat.lower()
print('Goodbye!')

