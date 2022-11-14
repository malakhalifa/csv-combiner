# Malak Khalifa - csv combiner 

# must handle more than two inputs, inputs with different columns, and large files  
# must print newly combined csv file to std output 

import sys 
import csv
import pandas as pd

output = open('output.csv', 'w+')

n = len(sys.argv)
for i in range(1, n):
    # safety checks - check that theres a next file and that min 2 files are given
    if (i >= n-1 or n < 2):
        break
    # create dataframes
    dfA = pd.read_csv(sys.argv[i])
    dfB = pd.read_csv(sys.argv[i+1])

    # find lengths of dataframes
    nA = len(dfA.index)
    nB = len(dfB.index)

    # merge common columns of 2 dataframes
    df = pd.merge(dfA, dfB, on=list(set(dfA.columns) & set(dfB.columns)), how = "outer")

    df["filename"] = nA * [sys.argv[i]] + nB * [sys.argv[i+1]]

    # save to new csv
    df.to_csv("output.csv", mode ='a', index = False)

# print new csv file with combined results     
f_input = open('output.csv', 'r')
with f_input: # implicitly closes file 
    reader = csv.reader(f_input)
    for row in reader:
        print(row)
