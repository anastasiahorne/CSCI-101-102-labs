#Anastasia Horne
#CSCI 102- Section G
#Week 2 - Lab A - Simple Calculator
#References: no one
#Time: 40 minutes

operand_one= 0.0
operand_two= 0.0
sum1= 0.0
differnece= 0.0
product= 0.0
quotient= 0.0
remiander= 0.0

operand_one= float(input('FIRST>'))
operand_two= float(input('SECOND>'))
sum1= operand_one + operand_two
difference= operand_one - operand_two
product= operand_one * operand_two
quotient= operand_one / operand_two
remainder= operand_one % operand_two

print( f'The sum of {operand_one} and {operand_two:.1f} is {sum1:.1f}')
print( f'The difference of {operand_one} and {operand_two:.1f} is {difference:.1f}')
print( f'The product of {operand_one} and {operand_two:.1f} is {product:.1f}')
print( f'The quotient of {operand_one} and {operand_two:.1f} is {quotient:.0f}')
print( f'The remainder of {operand_one} and {operand_two:.1f} is {remainder:.2f}')

