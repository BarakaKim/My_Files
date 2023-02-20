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
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SNo", "Name", "Subject"])
#     writer.writerow([1, "Ash Ketchum", "English"])
#     writer.writerow([2, "Gary Oak", "Mathematics"])
#     writer.writerow([3, "Brock Lesner", "Physics"])

row_list = [["SNo", "Name", "Subject"],
             [1, "Ash Ketchum", "English"],
             [2, "Gary Oak", "Mathematics"],
             [3, "Brock Lesner", "Physics"]]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(row_list)


print ('READ THE STUDENT.CSV')
print ('====================================================')
with open ('students.csv') as f2:
    csv.reader (f2)
    for row in f2:
        print (row)


print ('CREATE CSV FROM DICTIONARY USING DictWriter')
print ('====================================================')
data = {'A':'X1', 'B':'X2', 'C':'X3'}
with open('my_file3.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)
print ('\t')

print ('CREATE CSV FROM DICTIONARY USING PANDAS')
print ('====================================================')
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}
df = pd.DataFrame(x)
print (df)
df.to_csv ('maua.csv', index=False)
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
