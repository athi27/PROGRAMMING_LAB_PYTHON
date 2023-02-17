import csv
cars=[{'No.':1,'Company':'Benz','Model':'488GTB'},{'No.':2,'Company':'Ferarri','Model':'588GTB'}]
csvfile=open('Names.csv','w')
field_names=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()
csv_file=open('Names.csv','r')
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line,end="")