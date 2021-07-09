# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv


data_of_table_1 = []
with open("VF9.csv", 'r') as file:  #open table 1
    data_of_table_1=file.readlines()
    print("Reading table 1 successfully")

data_of_table_2 = []
with open("VE9_.csv", 'r') as file:  #open table 2
    data_of_table_2=file.readlines()
    print("Reading table 2 successfully")



output_table_data = [] # this will be the data to write into a third table
not_found_rqs=[]
found_rqs=[]
found = False
for row_from_table_1 in data_of_table_1:
    elements_in_row_1 = row_from_table_1.split(';')
    print("RoW VF9")
    print(elements_in_row_1)
    for row_from_table_2 in data_of_table_2:
        elements_in_row_2 = row_from_table_2.split(';')
        print("RoW Ve9")
        print(elements_in_row_2)
        if (elements_in_row_1[2][-19:] == elements_in_row_2[2][-19:]):
            elements_in_row_1[6] = elements_in_row_2[6]
            elements_in_row_1[7] = elements_in_row_2[7]
            elements_in_row_1[8] = elements_in_row_2[8]
            elements_in_row_1[9] = elements_in_row_2[9]
            elements_in_row_1[12]=elements_in_row_1[12].strip()
            output_table_data.append(elements_in_row_1)
            found_rqs.append(elements_in_row_1[0])
            break
    not_found_rqs.append(elements_in_row_1[0])
    #print(str(idx) +" / "+ str(len(data_of_table_1)))


notrq=[]
print("not found rqs")
for i in not_found_rqs:
    if i in found_rqs:
        continue
    notrq.append(i)


for rq in notrq:
    for row1 in data_of_table_1:
        elements=row1.split(";")
        if (rq == elements[0]):
            elements[12]=elements[12].strip()
            output_table_data.append(elements)

with open('output.csv', 'w', newline='') as csvfile:   #writing the data into the output table
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in output_table_data:
        spamwriter.writerow(row)
        #print(row)




id=0
#for elem in notrq:
 #   print(str(id))
  #  print (elem)
   # id=id+1

