import csv
from modules.packages import *
from modules.hash_table import *

hash_table = ChainingHashTable()
distance_data = []
address_data = []

# parse the packages csv file
def import_packages(filename):
    with open(filename) as csv_file:
        packages_csv = csv.reader(csv_file, delimiter=",")
        # loop through each row in the csv file
        # O(n)
        for row in packages_csv:
            # storing values into variables to pass into insert function and package object
            package_id = int(row[0])
            del_address = row[1]
            del_city = row[2]
            del_state = row[3]
            del_zip = int(row[4])
            del_deadline = row[5]
            del_weight = int(row[6])
            special_notes = row[7]
            # insert package id as an integer for the key and a package object as the value
            hash_table.insert(package_id, Package(package_id, del_address, del_city, del_state, del_zip, del_deadline, del_weight, special_notes))


# parse the distance csv file
def import_distances(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # store each row from csv file into distance_data list
        # O(n)
        for row in reader:
            distance_data.append(row)
        # iterate over the rows and columns to fill in the missing values from the csv
        # this creates a complete distance table
        # O(n^2)
        for i in range(len(distance_data)):
            for j in range(len(distance_data)):
                distance_data[i][j] = distance_data[j][i]


# parse the address csv file
def import_addresses(filename):
    with open(filename) as csv_file:
        addresses_csv = csv.reader(csv_file, delimiter=",")
        # loop through each row in the csv file
        # O(n)
        for row in addresses_csv:
            # append only the address (element 1, index 0) to the list
            address_data.append(row[0])
            # print(address_data)