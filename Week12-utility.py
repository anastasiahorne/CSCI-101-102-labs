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
