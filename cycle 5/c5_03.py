import csv
csv_file1=open('studentdetails.csv','r')
csv_reader=csv.reader(csv_file1)
for line in csv_reader:
    print(line)