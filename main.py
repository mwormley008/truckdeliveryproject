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