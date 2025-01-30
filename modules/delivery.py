import datetime

from modules.trucks import *
from modules.import_csv import *

# manually loading trucks and inputting departure times
truck1 = Truck([13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],
                  datetime.timedelta(hours=8, minutes=0, seconds=0), "1")
truck2 = Truck([3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39], datetime.timedelta(hours=9, minutes=5, seconds=0),
                  "2")
truck3 = Truck([9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],
                    datetime.timedelta(hours=10, minutes=20, seconds=0), "3")

trucks = [truck1, truck2, truck3]


def address_lookup(address):
    return address_data.index(address)


def distance_between(address1, address2):
    index1 = address_lookup(address1)
    index2 = address_lookup(address2)
    if index2 < index1:
        index1, index2 = index2, index1
    return float(distance_data[index1][index2+1])


def min_distance(truck):
    distances = []
    # loop through undelivered packages in the truck
    for element in truck.undelivered:
        # Create a list of possible distances between current location and all other possible locations
        dist = distance_between(truck.current_address, hash_table.search(element).del_address)
        distances.append(float(dist))
    # Minimum of that list is the shortest distance and therefore the Nearest Neighbor
    minimum_distance = min(distances)
    index_of_minimum = distances.index(minimum_distance)
    return index_of_minimum, minimum_distance



def nearest_neighbor_delivery(truck):
    # Packages in truck but not delivered are "en route"
    for element in truck.undelivered:
        hash_table.search(element).status = "Status: En route"
        hash_table.search(element).departure_time = truck.depart_time
        truck.current_time = truck.depart_time
    # Find the shortest distance using min_distance(), add 
    while len(truck.undelivered) > 0:
        # Find the nearest neighbor to travel to next
        index_of_nearest, shortest_distance = min_distance(truck)
        truck.current_address = hash_table.search(truck.undelivered[index_of_nearest]).del_address

        # Increment mileage
        truck.miles_traveled += shortest_distance
        # Update time for each delivery
        truck.current_time += datetime.timedelta(hours=shortest_distance / 18)
        
        # Change status of the delivered package to "Delivered"
        hash_table.search(truck.undelivered[index_of_nearest]).status = "Status: Delivered"
        # Change delivered time of the delivered package to the time it was delivered
        hash_table.search(truck.undelivered[index_of_nearest]).delivered_time = truck.current_time
        # Remove delivered package from the list of undelivered packages, then add it to the list of delivered packages
        truck.delivered.append(truck.undelivered[index_of_nearest])
        truck.undelivered.remove(truck.undelivered[index_of_nearest])

    # Add mileage to return to the place the truck started at from the last delivery location.
    return_trip_mileage = distance_between(hash_table.search(truck.delivered[len(truck.delivered) - 1]).del_address,truck.start_address)
    truck.miles_traveled += return_trip_mileage
    truck.miles_traveled = round(truck.miles_traveled, 1)
    truck.current_time += datetime.timedelta(hours=return_trip_mileage / 18)