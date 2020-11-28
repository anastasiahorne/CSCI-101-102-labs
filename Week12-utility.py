#Anastasia Horne
#CSCI 102 – Section G
#Week 12 - Utility using Git and Incremental Development
#References: None
#Time:  minutes

def load_file(file_name):
    file=open(file_name,'r')
    file_list= file.readlines()
    return file_list
    file.close()



def update_string(string_1,string_2,index):
    new_string= string_1[0:index]
    new_string+=string_2
    new_string+= string_1[(index+1):]
    print(new_string)



def find_word_count(list_given,string):
    count=0
    for i in range(0,len(list_given)):
       single_list= list_given[i].split()
       for k in range(0,len(single_list)):
           if single_list[k]==string:
               count+=1
    return count
