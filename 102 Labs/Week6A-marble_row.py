#Anastasia Horne
#CSCI 102 – Section G
#Week 6 - Lab A - Lost Marbles
#References: None
#Time: 15 minutes
print('Input a string of X\'s and O\'s:')
marble_str= input('MARBLES>')
marble_location=[]
marble=''
for i in range(0,len(marble_str)):
    marble=marble_str[i]
    if marble is 'O':
        marble_location.append(i)

    elif marble is 'X':
        continue
print('Here are your marble locations:')
print('OUTPUT',marble_location)
