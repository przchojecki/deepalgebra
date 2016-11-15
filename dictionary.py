#import tensorflow



#for importing files
import csv 


#input .txt file (with LaTeX code) - each line 

results = []
with open('inputfile.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)


#translate into Coq; use SyntaxNet for semantical analysis 


#output .txt file (with Coq code)
