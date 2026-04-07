#  Payton Sales
#  4 / 4 / 2026
#  
#  Module 3 Lab - Case Study: Lists, Functions, and Classes
#  ------------------------------------------------------------
#  The goal of this Lab is to create a program that utilizes a Superclass
#  and Subclass to store a user's vehicle information/attributes and 
#  print them back to the user in an organized fashion.


# Superclass called vehicle
# Contains attribute for vehicle_type
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass inherits attributes from Superclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):

        # Get vehicle_type from Vehicle Superclass
        super().__init__(vehicle_type)
        
        # Define new attributes for Vehicle
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Main Program
# Set Vehicle type to "car"
vehicle_type = "car"

# Get user input for Vehicle attributes
print("\nLet's input some details for your vehicle! ")

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 / 4): ")
roof = input("Enter the type of roof (solid roof / sun roof): ")

# Initialize the car object and assign attributes
car = Automobile(vehicle_type, year, make, model, doors, roof)

# Print Vehicle attributes
print("\n-----------  Vehicle Details  -----------")
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors on vehicle:", car.doors)
print("Type of roof on vehicle:", car.roof)
print("-----------  Vehicle Details  -----------\n")