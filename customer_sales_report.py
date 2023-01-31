#Sales report

#Import Modules
import csv
import os

#global constants
SALESFILE = 'sales.csv'
TEMPFILE = 'salesreport.csv'

#main
def main():
    #open files
    infile = open(SALESFILE, 'r', newline= '')
    outfile = open(TEMPFILE, 'w', newline= '')

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)

    #headers
    new_header = ['Customer ID', 'Total']
    writer.writerow(new_header)

    #loop through reader
    for row in reader:
        cust_id = int(row[0])
        sub_total = float(row[3])
        tax_amount = float(row[4])
        freight = float(row[5])

        calc_total = round(sub_total + tax_amount + freight, 2)

 
            
        new_row = [cust_id, calc_total]
        writer.writerow(new_row)
            
     
        
    #close files
    infile.close()
    outfile.close()

main()