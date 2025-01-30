from modules.delivery import *


# function to convert a user input of time in string format into a datetime object
def convert_time(user_time):
    (h, m, s) = user_time.split(":")
    h = int(h)
    m = int(m)
    s = int(s)
    return datetime.timedelta(hours=h, minutes=m, seconds=s)


def user_interface():
    # displays the total distance traveled by the trucks
    total_distance = 0
    for i in trucks:
        total_distance += i.miles_traveled
    rounded_total_distance = round(total_distance, 1)
    print(f"Total distance traveled for all trucks: {rounded_total_distance} miles")
    for truck in trucks:
        print(f"\nTruck {truck.truck_id} Packages:")
        print(truck.delivered)
    print("\n Select option")
    ui_running = True
    # runs until the user quits the interface
    while ui_running:
        print("1 - Get single package details")
        print("2 - Get details from all packages")
        print("3 - Show total miles driven by trucks")
        print("0 - Exit program")
        try:
            option = int(input("[?]: "))
            if option == 0:
                try:
                    print("Ending program")
                    ui_running = False
                except:
                    print("Invalid input.")
            elif option == 1:
                try:
                    # take the user input for a time in the correct format, else send error message
                    user_time = input("enter time with format, HH:MM:SS: ")
                    # convert the user input from string to a datetime object
                    converted_time = convert_time(user_time)
                    # take the user input for package ID
                    lookup_id = int(input("enter package ID: "))
                    # search hash table for the package object
                    package = hash_table.search(lookup_id)
                    # print details to the screen
                    print(package.package_lookup(converted_time))
                except:
                    print("Invalid input.")
            elif option == 2:
                try:
                    user_time = input("enter time with format, HH:MM:SS: ")
                    converted_time = convert_time(user_time)
                    # loop through all packages in hash table
                    for element in range(1, 41):
                        package = hash_table.search(element)
                        print(package.package_lookup(converted_time))
                except:
                    print("Invalid input.")
            elif option == 3:
                try:
                    print("Total distance traveled for all trucks: {} miles".format(rounded_total_distance))
                except:
                    print("Invalid input.")
            else:
                print("invalid input.")
        except:
            print("invalid input.")