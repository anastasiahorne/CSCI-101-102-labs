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
    
