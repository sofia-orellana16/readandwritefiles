#Employee Pay

#Import Modules
import csv
import os

#global constants
EMPFILE = 'EmployeePay.csv'

#main
def main():
    #open file
    infile = open(EMPFILE, 'r', newline='')
    reader = csv.reader(infile)

    #read field names
    fields = next(reader)
    print(format(fields[0], '<5'), format(fields[1],'<12'),format(fields[2],'<12'), format(fields[3],'<10'),format(fields[4], '<10'))
    print()

    #loop through reader
    for row in reader:
        print(format(row[0], '<5'), format(row[1],'<12'), format(row[2], '<12'), format(row[3], '<10'), format(row[4], '<10'))
    
    #close file
    infile.close()

main()

