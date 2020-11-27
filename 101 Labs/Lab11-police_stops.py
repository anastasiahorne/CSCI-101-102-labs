#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 11
#References: None 
#Time:  120 minutes






def read_csv(csvfile):
    import csv
    row_list=[]
    with open(csvfile,'r') as file:
        file_reader= csv.reader(file, delimiter=',')
        for row in file_reader:
            return row
 #I waited for an hour in the zoom call to get help but there were so many people ahead of me it wasn't gonna get to me anytime soon.
    #I couldn't figure out how to return all the rows. If I gave a print statement it would print the entire contents of the file. But if I do just return row it only returns the headers.
        #If I try to append each row to a list it is unable to deocde. I tried differnet decoding methods but I frankly have no clue what they do or how they work, so none worked.
'''rows= read_csv('aurora_police.csv')'''
'''def stops_by_race(rows, subject_race):
    amount_race=0
    if subject_race in row:
        amount_race+=1
    if subject_race=='ALL':
        print('172929')
    print(amount_race)'''
