# Design a store using OOP methodologies

from classes import Latlon

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, costs ${self.price}"

class Department:
    # products will be list of tuples with signature (string, int)
    def __init__(self, name):
        self.name = name
        self.products = [Product(p[0], p[1]) for p in products]

    def __str__(self):
        return f"No products available in the {self.name} department, yet."

# what does the store look like
# what attributes
# name
# location
# categories of products
# products

class Store:
    def __init__(self, name, lat, lon, categories):
        self.name = name
        self.location = Latlon(lat, lon)
        self.departments = [Departments(d) for d in departments]

    # add an __str__ method so that we can observe our Store instance
    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.departments}"

store = Store("LambdaStore", 44.13544, -121.123124, ["Clothing", "Cookware", "Books", "Sporting Goods"])
print(store)

# we want to add departments
# let's take input grom the user and have themspecify departments by the department's
# index in the departments list

selection = input("Select the number of department")
print("The user selected " + store.departments[int(selection)])


# wrap all this logic in a while loop so that we can keep giving selections
# instead of having re-run the program every time
while True:
    slection = input("Select the number of a department or type 'exit' to leave: ")

    if selection == "exit":
        print("Thanks for shopping with us!")
        Break

# add error handling so that when a user inputs a department for a non-existent
# department, we'll notify them that the department doesn't existent
try:
    # caasting might cause an error
    selection = int(selection)
    if selection >= len(store.departments):
        print("That's not a valid department")
    elif selection >= 0 and selection < len(store.departments):
        print(f"{store.departments[selection]}")
    else:
        print("Department numbers are positive")
except ValueError:
    # the user didin't give us a value that could be cast as a number
    print("Please enter your choise as a number")
