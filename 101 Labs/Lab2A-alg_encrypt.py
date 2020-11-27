#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 2A
#References: no one
#Time: 60 minute

List_1= str(input('LIST1>'))
List_2= str(input('LIST2>'))
List_3= str(input('LIST3>'))
List_4= str(input('LIST4>'))
List_5= str(input('LIST5>'))
b= int(len(List_3)/2)
print('Your encrypted message is:')
print('OUTPUT', f'{List_5[0:2]} {List_1[-2]}{List_1[-1]}{List_1[0:-2]}{List_2[0:-2]}{List_3[b:]}', end= '')
print(f'{List_4[2]}{List_4[1]}{List_4[0]}{List_4[3:]} {List_5[2:]}')

