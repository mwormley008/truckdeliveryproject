# Name: Michael Wormley
# Student id:012418005

# this is a program designed to practice using Data Structures and Algorithm
# The task is to find an efficient routing mechanism to deliver different packages

from modules.menu import *


class Main:
    print("WGUPS Menu\n")

    # import information from given CSV files
    import_packages("csv_files/packages.csv")
    import_distances("csv_files/distances.csv")
    import_addresses("csv_files/addresses.csv")

    # calling delivery functions for each truck from delivery.py module
    delivery(truck_one)
    delivery(truck_two)
    delivery(truck_three)

    # start of program's user interface from menu.py module
    start_ui()