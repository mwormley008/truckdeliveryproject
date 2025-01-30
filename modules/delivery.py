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
    # loop through elements in truck's array of packages not delivered
    for element in truck.undelivered:
        # find the distance between the truck's current address and every other element in the array
        dist = distance_between(truck.current_address, hash_table.search(element).del_address)
        # add that distance in miles to the distances array
        distances.append(float(dist))
    # find the minimum value in the array of distances
    minimum_distance = min(distances)
    # find the index of the next closest address
    index_of_minimum = distances.index(minimum_distance)
    return index_of_minimum, minimum_distance



def nearest_neighbor_delivery(truck):
    # set packages in truck as en route
    for element in truck.undelivered:
        hash_table.search(element).status = "en route"
        hash_table.search(element).departure_time = truck.depart_time
        truck.current_time = truck.depart_time
    # loop through every package on the truck in the undelivered array
    while len(truck.undelivered) > 0:
        # find the shortest distance from current_address of truck to any package
        index_of_nearest, shortest_distance = min_distance(truck)
        truck.current_address = hash_table.search(truck.undelivered[index_of_nearest]).del_address
        # add mileage to package to truck's total milage
        truck.miles_traveled += shortest_distance
        # update current time as each package is delivered
        truck.current_time += datetime.timedelta(hours=shortest_distance / 18)
        # Change status of the delivered package to "delivered"
        hash_table.search(truck.undelivered[index_of_nearest]).status = "delivered"
        # Change delivered time of the delivered package to the time it was delivered
        hash_table.search(truck.undelivered[index_of_nearest]).delivered_time = truck.current_time
        # Removed delivered package from the list of undelivered packages, then add it to the list of delivered packages
        truck.delivered.append(truck.undelivered[index_of_nearest])
        truck.undelivered.remove(truck.undelivered[index_of_nearest])
    # add mileage from last package on truck back to the hub
    dist_back_to_hub = distance_between(hash_table.search(truck.delivered[len(truck.delivered) - 1]).del_address,
                                        truck.start_address)
    truck.miles_traveled += dist_back_to_hub
    truck.miles_traveled = round(truck.miles_traveled, 1)
    truck.current_time += datetime.timedelta(hours=dist_back_to_hub / 18)