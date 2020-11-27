#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 4
#References: no one
#Time: 80 minutes

filing_status= str(input('STATUS>'))
income= int(input('INCOME>'))
#tax brackets maximum for filed single 
b1_tax=.1*9325 
b2_tax=.15*(37950-9325)
b3_tax=.25*(91900-37950)
b4_tax=.28*(191650-91900)
b5_tax=.33*(416900-191650)
b6_tax=.35*(418400-416900)

#tax brackets maximum for filed joint
b1j=.1*18650
b2j=.15*(75900-18650)
b3j=.25*(153100-75900)
b4j=.28*(233350-153100)
b5j=.33*(416900-233350)
b6j=.35*(470700-416900)




#if time allows check to see if there's an easier cleaner way to do this, can i
#take the print statements and make them 1 line



if filing_status=='single':
    if income<=9325:
        tax_amt= .1 * 9325
        per_o_income=(tax_amt/income) *100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=37950:
        tax_amt= ((income-9325)*.15)+ b1_tax
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=91900:
        tax_amt=((income-37950)*.25) + b1_tax + b2_tax
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=191650:
        tax_amt=((income-91900)*.28) +b1_tax + b2_tax + b3_tax
        per_o_income= (tax_amt/income) *100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=416900:
        tax_amt=((income-191650)*.33) +b1_tax + b2_tax + b3_tax + b4_tax
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=418400:
        tax_amt=((income-416900)*.35)+ b1_tax + b2_tax + b3_tax + b4_tax +b5_tax
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    else:
        tax_amt=((income-418400)*.396)+ b1_tax + b2_tax + b3_tax + b4_tax +b5_tax + b6_tax
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
else:
    if income<=18650 :
        tax_amt= (income*.1)
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=75900 :
        tax_amt=((income-18659)*.15)+ b1j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=153100 :
        tax_amt=((income-75900)*.25)+b1j+b2j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=233350 :
        tax_amt=((income-153100)*.28)+b1j+b2j+b3j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=416900 :
        tax_amt=((income-233350)*.33)+b1j+b2j+b3j+b4j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    elif income<=470700 :
        tax_amt=((income-416900)*.35)+b1j+b2j+b3j+b4j+b5j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
    else:
        tax_amt=((income-470700)*.396)+b1j+b2j+b3j+b4j+b5j+b6j
        per_o_income= (tax_amt/income)*100
        print('OUTPUT',int(tax_amt))
        print(f'OUTPUT {per_o_income:.2f}')
        
    
        

