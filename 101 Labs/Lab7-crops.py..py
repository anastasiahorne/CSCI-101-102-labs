#Anastasia Horne
#CSCI 101 – Section A
#Python Lab 7
#References: None
#Time: 280 minutes






n= int(input('ROWS>'))
m= int(input('COLUMNS>'))
field=[]
row_list=[]
for i in range(n):
    row_str=(input(f'ROW{i}>'))
    for z in range((m*2)):
        if z%2!=0:
           row_list.append(row_str[z]) 
            
        else:
            continue
        
    field.append(row_list)
    row_list=[]
    
print(field)
non_water=[]
area= n*m
row=0
counter=0
check= True
bottom_row= row+1
above_row= row-1
for i in range(m):
    if field[row][i]== 'c':
        if n>2 and (1<=row<=(n-2)):
            for k in range(i-1,i+2):
                if field[row][k]=='w':
                    break
                else:
                    counter+=1
                    continue
            for a in range(i-1,i+2):
                if field[bottom_row][a]=='w':
                    break
                else:
                    counter+=1
                    continue
            for b in range(i-1,i+2):
                if field[above_row][b]=='w':
                    break
                else:
                    counter+=1
                    continue
        
            if counter==9:
               non_water.append(field[row][i])
               check= False
        elif n==1:
            for c in range(i-1,i+2):
                if field[row][c]=='w':
                    break
                else:
                    counter+=1
                    continue
            if counter==3:
               non_water.append(field[row][i])
               check= False

        elif n==2:
            if row==0:
                for d in range(i-1,i+2):
                    if field[row][d]=='w':
                        break
                    else:
                        counter+=1
                        continue
                for e in range(i-1,i+2):
                    if field[bottom_row][e]=='w':
                        break
                    else:
                        counter+=1
                        continue
                if counter==5:
                   non_water.append(field[row][i])
                   check= False
            elif row==1:
                for f in range(i-1,i+2):
                    if field[row][f]=='w':
                        break
                    else:
                        counter+=1
                        continue
                for g in range(i-1,i+2):
                    if field[above_row][g]=='w':
                        break
                    else:
                        counter+=1
                        continue
                if counter==5:
                   non_water.append(field[row][i])
                   check= False

    if n>1:
        row+=1
    else:
        break

                
    
























        
        


if check== True:
    print('OUTPUT True')
if check== False:
    print('OUTPUT False')
    print(f'OUTPUT {non_water}')
    
    
  
