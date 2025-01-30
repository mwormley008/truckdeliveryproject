# Name: Michael Wormley
# Student id:012418005

# this is a program designed to practice using Data Structures and Algorithm
# The task is to find an efficient routing mechanism to deliver different packages

from modules.menu import *


class Main:
    print("WGUPS Menu\n")

    # import information from given CSV files
    import_csv_files()

    # calls the delivery function for each truck in the list of the trucks
    for i in trucks:
        nearest_neighbor_delivery(i)

    # CLI User interface is initiated
    user_interface()

""" The way this program basically flows is that there are classes to construct objects for the packages and trucks, as well as the hash table that will store all of the
packages. The import_csv module imports all of the information from the given CSV files and then creates packages and tables of delivery information. Once this has occurred,
the delivery routine is run for each truck, which uses a "Nearest Neighbor" algorithm to determine where each package should go. The user interface allows the user to 
inspect information about how the program was run and request more information about the packages."""
