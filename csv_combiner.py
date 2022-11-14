# Malak Khalifa - csv combiner 

# must handle more than two inputs, inputs with different columns, and large files  
# must print newly combined csv file to std output 

import sys 
import csv

# takes in two csv files, returns new csv file (result of combining them)
def csv_combiner(filename, combined_data):

    # read csv file 
    f_input = open(filename, 'r')
    read_csv = csv.reader(f_input)
    with f_input: # implicitly closes file
        for row in read_csv:
            # edge case - only include 1 header at top 
            if len(combined_data) >= 1 and (row[0]) in combined_data[0]: 
                pass
            else:
                # if header
                if (len(combined_data) == 0):
                    row.append("filename")
                else:
                    # add additional column with filename to the row 
                    row.append(filename) 
                # append new row
                combined_data.append(row) 


# find number of arguments
n = len(sys.argv)
combined_data = [] 

# edge case - handling multiple csv files
for i in range(1, n):
    # call combiner function
    csv_combiner(sys.argv[i], combined_data)

# create new csv file with combined results 
with open('combined.csv', 'w+') as f_output:
    for row in (combined_data):
        for cell in (row):
            # remove comma at end of each row 
            if (cell == row[-1]):
                f_output.write("\"" + cell + "\"")
            else:
                # write to file 
                f_output.write("\"" + cell + "\"" + ",")
                # print to std ouput
                print (cell)
        f_output.write("\n")

    # make sure it's printing well to std output 
    # edge case - handling different columns 

    # test with: multiple csv files - should work 







