#Anastasia Horne
#CSCI 101 – Section A
#Python Lab 3
#References: no one
#Time: 20 minutes

hours=int(input('HOURS>'))
minutes=int(input('MINUTES>'))

if minutes >40:
    new_minute= minutes-40
    new_hour=hours
    print(f'OUTPUT {new_hour} {new_minute}')

elif minutes==40:
    new_minute= 00
    new_hour=hours
    print(f'OUTPUT {new_hour} 00')

elif hours==0:
    new_hour=23
    new_minute=60-(40-minutes)
    print(f'OUTPUT {new_hour} {new_minute}')

else:
    new_hour=hours-1
    new_minute=60-(40-minutes)
    print(f'OUTPUT {new_hour} {new_minute}')
    
