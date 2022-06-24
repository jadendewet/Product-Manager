# Imports Tabulate 


# Creates Shoe class 
class Shoe():

    # Creates the constructor method
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product 
        self.cost = int(cost)
        self.quantity = int(quantity)

        self.value_of_item = self.cost * self.quantity


    # Creates a repr method to visualise the data rather than have it as its place in memory
    def __repr__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"


    # A getter method to return the quantity of the object
    def get_quantity(self):
        return self.quantity


    # A getter method to return the price of the object
    def get_price(self):
        return self.cost


    # A getter method to return the product code of the object
    def get_code(self):
        return self.code


    # A getter method to return the product name of the object
    def get_product(self):
        return self.product


    # A getter method to return the country of the object
    def get_location(self):
        return self.country


    # A setter method to set a new value to the price of the object
    def set_price(self,new_cost):
        self.cost = new_cost


    # A getter method to return the total value of the stock of the object
    def get_value_per_item(self):
        return self.value_of_item


    # A setter method to set a new amount to the quantity of the object 
    def set_quantity(self, extra_stock):
        self.quantity = self.quantity + extra_stock


# This function splits the data in the file, appends it to a temporary list before tabulating the data for the user to see
def read_data():
        try:

            file = open("inventory.txt","r+")
            for stock in file:
                location = stock.split(',')[0]
                code = stock.split(',')[1]
                product = stock.split(',')[2]
                price = stock.split(',')[3]
                quantity = stock.split(',')[-1]

                temp_list =  [location, code, product, f"R{price}", quantity]
                full_stock.append(temp_list)

            # I had to remove the first line of the file as it was repetitive, hence I used the pop function
            full_stock.pop(1)
            #print(tabulate(full_stock))

        except FileNotFoundError:
            print("The file not found ")


# This function finds the product with the lowest stock in the list. It asks for user input and sets quantity to said input
def lowest_stock(obj_list):
    lowest = obj_list[0]
    for products in obj_list:
        if lowest.get_quantity() > products.get_quantity():
            lowest = products

    print("")
    print(f"Product: \t{lowest.get_product()}")
    print(f"Quantity: \t{lowest.get_quantity()}")
    print(f"Price:   \tR{lowest.get_price()}")
    print("")

    new_stock_value = int(input("How much stock will be added: "))
    lowest.set_quantity(new_stock_value)
    print("Stock Added")


# This function asks for user input - If the user enters a code that matches with a product code in the list it will display the information about the product
def find_product(obj_list):
    prod_code = input("Enter the code of the product you would like to find: ")
    print("")
    for product in obj_list:
        if product.get_code() == prod_code:
            print(f"Product: \t{product.get_product()}")
            print(f"Quantity: \t{product.get_quantity()}")
            print(f"Price:   \tR{product.get_price()}")


# This function will find the product with the most stock in the list - ask the user for the new price of it, and set the price to said input
def most_stock(obj_list):
    highest = obj_list[0]
    for products in obj_list:
        if highest.get_quantity() < products.get_quantity():

            highest = products
            print("")
            print(f"Product: \t{highest.get_product()}")
            print(f"Quantity: \t{highest.get_quantity()}")
            print(f"Price:   \tR{highest.get_price()}")
            print("")

    new_price = int(input("Enter the new price: "))
    highest.set_price(new_price)
    print("")
    print(f"New price added")


# This function will tabulate the data in the object list and display them in a pleasing, more detailed manner
def show_table(obj_list):
    for object in obj_list:
        location = object.get_location()
        code = object.get_code()
        product = object.get_product()
        price = object.get_price()
        quantity = object.get_quantity()
        value_per_item = object.get_value_per_item()

        temp_list = [location, code, product, f"R{price}", quantity, f"R{value_per_item}"]
        table_list.append(temp_list)

    print(tabulate(table_list, headers="firstrow"))


# This function is used to display the menu 
def shoe_menu():
    options = "1) Read data \n2) Find product from code \n3) Find highest stock and set sale price \n4) Restock product with lowest stock \n5) Display overview \n6) Exit"
    print(options)

# Created 2 header lists used for tabulating data 
full_stock = [["Location", "Code", "Product", "Price", "Quantity"]]
table_list = [["Location", "Code", "Product", "Price", "Quantity", "Value of Stock"]]

# Created an object list
obj_list = []

# Creates instances of the Shoe class and appends them to the list
shoe_1 = Shoe("France","SKU221167","Jordan",3500,13)
obj_list.append(shoe_1)

shoe_2 = Shoe("Spain","SKU223666","Air_Max",2500,12)
obj_list.append(shoe_2)

shoe_3 = Shoe("Asia","SKU298761","Blazers",3000,99)
obj_list.append(shoe_3)

shoe_4 = Shoe("Canada","SKU223907","Air_Force",1750,17)
obj_list.append(shoe_4)

shoe_5 = Shoe("Brazil", "SKU221946" ,"Dunks",4000,5)
obj_list.append(shoe_5)

# Creates and sets a control variable to True
menu = True

# Displays the menu and requests user input
shoe_menu()
user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

# While True
while menu == True:

    # If the user enters 1 - the read data function will be executed, as well as display the menu and request user input
    if user_choice == 1:
        read_data()
        print("")
        shoe_menu()
        user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

    # If the user enters 2 - the find product function will be executed, as well as display the menu and request user input
    elif user_choice == 2:
        find_product(obj_list)
        print("")
        shoe_menu()
        user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

    # If the user enters 3 - the most stock function will be executed, as well as display the menu and request user input
    elif user_choice == 3:
        most_stock(obj_list)
        print("")
        shoe_menu()
        user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

    # If the user enters 4 - the read data function will be executed, as well as display the menu and request user input
    elif user_choice == 4:
        lowest_stock(obj_list)
        print("")
        shoe_menu()
        user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

    # If the user enters 5 - the show table function will be executed, as well as display the menu and request user input
    elif user_choice == 5:
        show_table(obj_list)
        print("")
        shoe_menu()
        user_choice = int(input("\nWhat would you like to do? \nPlease enter an option from the list: "))

    # If the user enters 6 - It will print a message and set the control variable to False to end the loop
    elif user_choice == 6:
        print("Thank you for using our program - Goodbye!")
        menu = False

    # Else prints the user has selcted an incorrect option
    else:
        print("You have selected an incorrect option")




