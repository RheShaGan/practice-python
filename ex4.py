#assigning a value to cars variable
cars = 100 
#creating variable for the number of seats in the car
space_in_a_car = 4.0
#creating a variable for the total number of drivers available
drivers = 30
#number of passengers
passengers = 90
#calculating the number of cars not used
cars_not_driven = cars - drivers
#calculating the cars driven which will be equivalent to the number of drivers available
cars_driven = drivers
#calculating carpool capacity based on cars driven and seats available in each car
carpool_capacity = cars_driven * space_in_a_car
average_passenges_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenges_per_car, "in each car.")