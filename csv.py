#CSV FILES
import csv
import pandas as pd

#create csv file from a given list
file = [['name: baraka', 'math: 97%'],['name: peter', 'math: 67%'],['name: jane', 'math: 98%']]
with open ('file.csv', 'w', newline='') as f:
    #f2 = csv.writer(f)
    #f2.writerows(file)
    csv.writer(f).writerows(file)

#read a csv file from the created file
print ('READ THE FILE.CSV')
print ('====================================================')
with open ('file.csv') as f1:
#     csv_file = csv.reader(f1)
#     for row in csv_file:
    csv.reader (f1)
    for row in f1:
        print (row)

print ('\t')

#create another csv file
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SNo", "Name", "Subject"])
    writer.writerow([1, "Ash Ketchum", "English"])
    writer.writerow([2, "Gary Oak", "Mathematics"])
    writer.writerow([3, "Brock Lesner", "Physics"])

print ('READ THE STUDENT.CSV')
print ('====================================================')
with open ('students.csv') as f2:
    csv.reader (f2)
    for row in f2:
        print (row)

print ('\t')
print ('READ CSV USING PANDAS')
print ('====================================================')
a = pd.read_csv ('train.csv')
print (type (a))
print (pd.DataFrame(a))
print ('\t')
print (a.keys().shape[0])
print (len (a.keys()))
print (a[['MSSubClass']]. head (10))
print (f"the number of unique classes:\n{a[['MSSubClass']].value_counts ().shape[0]}")
print (a[['MSSubClass']].sum())
print (a[['MSSubClass']].mean())
