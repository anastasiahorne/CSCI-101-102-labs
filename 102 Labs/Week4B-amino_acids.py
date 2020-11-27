#Anastasia Horne
#​CSCI 102 – Section G
#Week 4 - Lab B - Amino Acids
#References: no one
#Time:  40 minutes

Carbon= int(input('CARBON>'))
Hydrogen= int(input('HYDROGEN>'))
Nitrogen= int(input('NITROGEN>'))
Oxygen= int(input('OXYGEN>'))
Sulfur= int(input('SULFUR>'))

if Sulfur==1:
    print('OUTPUT C-3H-7N-1O-2S-0')
    print('OUTPUT Cysteine')
elif Oxygen==3:
        if Hydrogen==8:
            print('OUTPUT C-4H-8N-2O-3S-0')
            print('OUTPUT Asparagine')
        else:
            print('OUTPUT C-5H-10N-2O-3S-0')
            print('OUTPUT Glutamine')
elif Carbon==3:
    print('OUTPUT C-3H-7N-O-2S-0')
    print('OUTPUT Alanine')
elif Hydrogen==14:
    print('OUTPUT C-6H-14N-4O-2S-0')
    print('OUTPUT Arginine')
else:
    print('OUTPUT C-6H-9N-3O-2S-0')
    print('OUTPUT Histidine')

        
                    
        
