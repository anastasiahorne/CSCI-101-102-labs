#Anastasia Horne
#CSCI 102 – Section G
#Week 10 Lab
#References: None
#Time: 180 minutes


import csv
headers= ['Depth','Start Depth','End Depth', 'Average Depth','Formation']

with open('formations.csv', 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
        with open('formations_parsed.csv', 'w+', newline='') as csvfile:
            filewriter=csv.writer(csvfile)
            filewriter.writerow(headers)
            
        


#I spent that entire 3 hours figuring out how to do the headers correctly. I ran out of time to do the rest. Just gonna have to create time out of thin air.
    
    








