#Anastasia Horne
#CSCI 102 – Section G
#Week 11 Lab
#References: None
#Time: 100 minutes

def to_hex(dec_num):
    decimal= dec_num
    hex_list=[]
    if decimal==0:
        hex_list.append(str(decimal))
    else:
        while decimal>0:
            dec_char= decimal%16
            if dec_char>9:
                hex_char=['A','B','C','D','E','F']
                index= dec_char-10
                hex_list.append(hex_char[index])
            else:
                hex_list.append(str(dec_char))
            decimal=decimal//16
    hex_list.reverse()
    s=''
    hex_str=s.join(hex_list)
    if len(hex_str)!=2:
        hex_str= '0'+ hex_str
    return hex_str

def rgb_to_hex(rgb_tuple):
    rgb=rgb_tuple
    hex_list1=[]
    for i in range(0,3):
        in_hex= to_hex(rgb[i])
        hex_list1.append(str(in_hex))
    x=''
    rgb_to_hex_str=x.join(hex_list1)
    
