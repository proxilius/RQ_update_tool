# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv


data_of_table_1 = []
with open("tabla_egy.csv", 'r') as file:  #open table 1
    data_of_table_1=file.readlines()

data_of_table_2 = []
with open("tabla_ketto.csv", 'r') as file:  #open table 2
    data_of_table_2=file.readlines()

output_table_data = [] # this will be the data to write into a third table

for row_from_table_1 in data_of_table_1:
    elements_in_row_1 = row_from_table_1.split(',')
    for row_from_table_2 in data_of_table_2:
        elements_in_row_2 = row_from_table_2.split(',')
        if (elements_in_row_1[0] == elements_in_row_2[0]):
            elements_in_row_2[2] = elements_in_row_1[2]
            elements_in_row_2[3] = elements_in_row_1[3].strip()  # .strip() is needed to eliminate the \n character from the last element
            output_table_data.append(elements_in_row_2)
            break


with open('output.csv', 'w', newline='') as csvfile:   #writing the data into the output table
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in output_table_data:
        spamwriter.writerow(row)
        print(row)

