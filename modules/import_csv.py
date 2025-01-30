import csv
from modules.packages import *
from modules.hash_table import *

hash_table = ChainingHashTable()
distance_data = []
address_data = []

# these functions just loop through the csv files and then assign the information to variables in the format needed for their respective objects and functions

def import_packages(filename):
    with open(filename) as csv_file:
        packages_csv = csv.reader(csv_file, delimiter=",")
        
        for row in packages_csv:
            package_id = int(row[0])
            del_address = row[1]
            del_city = row[2]
            del_state = row[3]
            del_zip = int(row[4])
            del_deadline = row[5]
            del_weight = int(row[6])
            special_notes = row[7]
            hash_table.insert(package_id, Package(package_id, del_address, del_city, del_state, del_zip, del_deadline, del_weight, special_notes))



def import_distances(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        
        for row in reader:
            distance_data.append(row)

        # this part was a bit tricky for me so basically it's just going through the matrix of distances in the csv file
        # but the tricky part was that the first item in each list is the name of the location itself, and the second item 
        # is also address information so I needed to create the list so that as it iterated through it wouldn't disturb those pieces of 
        # information, so that's why the indices are offset the way that they are.
        for i in range(len(distance_data)):
            for j in range(0, len(distance_data)):
                distance_data[i][j+1] = distance_data[j][i+2]


# I made a separate address CSV because I thought that seemed easier than going through the distances CSV again.
def import_addresses(filename):
    with open(filename) as csv_file:
        addresses_csv = csv.reader(csv_file, delimiter=",")

        for row in addresses_csv:
            # append only the address (element 1, index 0) to the list
            address_data.append(row[0])

#imports all CSV files
def import_csv_files():
    import_packages("csv_files/packages.csv")
    import_distances("csv_files/distances.csv")
    import_addresses("csv_files/addresses.csv")