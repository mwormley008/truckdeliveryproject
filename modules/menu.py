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
            option = int(input("Selection: "))
            if option == 0:
                try:
                    print("Ending program")
                    ui_running = False
                except:
                    print("Invalid input.")
            elif option == 1:
                try:
                    # Requests time from user, then converts it to a datetime object
                    input_time = input("Enter time in format HH:MM:SS: ")
                    converted_time = convert_time(input_time)
                    # Requests package ID from user to search in the hash table and print details
                    lookup_id = int(input("enter package ID: "))
                    package = hash_table.search(lookup_id)
                    print(package.package_lookup(converted_time))
                except:
                    print("Invalid input.")
            elif option == 2:
                try:
                    input_time = input("Enter time in format HH:MM:SS: ")
                    converted_time = convert_time(input_time)
                    # Prints each package in hash table
                    for element in range(1, 41):
                        package = hash_table.search(element)
                        print(package.package_lookup(converted_time))
                except:
                    print("Invalid input.")
            elif option == 3:
                try:
                    print(f"Total distance traveled for all trucks: {rounded_total_distance} miles")
                except:
                    print("Invalid input.")
            else:
                print("invalid input.")
        except:
            print("invalid input.")