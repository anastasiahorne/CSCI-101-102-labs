#Anastasia Horne
#CSCI 102- Section G
#Week 5- Lab A- ASCII Carpet
#References: no one
# Time: 25 minutes

#Get the input for the specs of the rug
width= int(input('WIDTH>'))
height= int(input('HEIGHT>'))
character= input('CHARACTER>')

#set loop initial values
a=1
i=1

#how will we tell it to print the character x-times across, for the width
character_list=[]

#clarifying print statement
print(f'A rug with width {width}, and height {height}, using the character {character}, will look like:')

#While loops
while a<=width:
    character_list.append(character)
    a=a+1

while i<=height:
    print('OUTPUT',*character_list)
    i=i+1
    
