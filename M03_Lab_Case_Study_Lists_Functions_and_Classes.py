""" Student Name: Kyle Ingersoll
    File Name: M03_Lab_Case_Study_Lists_Functions_and_Classes.py
    Description: The program prompts the user to enter in data about a car and uses classes to store that data to later
                 display to the end user. Note, the two classes code is adapted from https://github.com/rwstorer/sdev220/blob/main/module03.ipynb.
    List and Description of the Variables: 
                                            car.vehicle_type = string variable that stores the vehicle type, i.e. car.
                                            auto.year = integer variable that stores the year the car was made
                                            auto.make = string variable that stores the name of the maker of the car
                                            auto.model = string variable that stores the model of the car
                                            auto.doors = integer variable that stores the number of doors that the car has, either 2 or 4 doors
                                            auto.roof: stores the type of roof the car has, either a solid or a sun roof

"""

# Initialize parent class
class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type
    
# Initialize child class
class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors
        self.roof: str = roof
   
# Introduction to the user for what the program will do      
print("This application accepts user input for a car and displays it to the end user.")

# populate car instance of Vehicle class with vehicle type
car: Vehicle = Vehicle(input('Enter a vehicle type:'))

# populate auto instance of Automobile class with the correct info. 
auto: Automobile = Automobile(car.vehicle_type, int(input("Enter the year the car was made:")), input("Enter the maker of the car:"), input("Enter the model of car:"), int(input("Enter the number of doors that the car has, either 2 or 4 doors:")), input("Enter the type of roof that the car has, solid or sun roof: "))

# make auto.roof lowercase for comparison
auto.roof = auto.roof.lower()

# Check car.doors and car.roof variables for correctness
if not(auto.doors == 2 or auto.doors == 4) or not(auto.roof == 'solid roof' or auto.roof == 'sun roof'):
    # Create entry loop to enforce conditions on data entry
    while True:
        # reenter data
        auto.doors = int(input("Enter the number of doors that the car has, either 2 or 4 doors:"))
        auto.roof = input("Enter the type of roof that the car has, solid or sun roof: ")
        # make car.roof lowercase for comparison
        auto.roof = auto.roof.lower()
       
        # double check data
        if not(auto.doors == 2 or auto.doors == 4) or not(auto.roof == 'solid roof' or auto.roof == 'sun roof'):
            continue
        else:
            break

        

# print out information about the car on screen
print("Vehicle type:", car.vehicle_type)
print("Year:", auto.year)
print("Make:", auto.make)
print("Model:", auto.model)
print("Number of doors:", auto.doors)
print("Type of roof:", auto.roof)
        