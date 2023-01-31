#Customer Country

#import modules
import csv
import os

#global constants
CUSTFILE = 'customers.csv'
TEMPFILE = 'customer_country.csv'

#main----------------------------
def main():
    print("Customer's Country List")

    #open file
    infile = open(CUSTFILE, 'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    fields = next(reader)

    #loop through rows
    for row in reader:
        first_name = row[1]
        last_name = row[2]
        country = row[4]

        new_row = [first_name, last_name, country]
        writer.writerow(new_row)

    #close files
    infile.close()
    outfile.close()

main()




    


