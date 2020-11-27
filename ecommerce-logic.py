import json
class Ecommerce:
    def __init__(self):
        pass
    def get_all_items(self):
        with open("ecommerce.json") as file:
            old_data = json.load(file)
        for n in range(0, len(old_data)):
            print("Item: {}\nPrice: {}\nAvailable stock: {}\nDescription: {}\n------------------------------".format(old_data[n]["item"], old_data[n]["price"], old_data[n]["availableStock"], old_data[n]["description"]))
    def add_item(self):
        new_item = input("Enter the name of a new item : ")
        new_price = int(input("Enter the price of the new item : "))
        new_availablestock = int(input("Enter the available stock of the new item : "))   
        new_description = input("Enter the description of the new item : ")
        data = {
            "item" : new_item,
            "price" : new_price,
            "availableStock" : new_availablestock,
            "description" : new_description
        }
        with open("ecommerce.json") as file:
            old_data = json.load(file)
        old_data.append(data)
        with open("ecommerce.json", "w") as file:
            json.dump(old_data, file, indent=4)
        print("Succesfully added new item")
    def remove_item(self):
        with open("ecommerce.json") as file:
            old_data = json.load(file)
        for n in range(0, len(old_data)):
            print("{}. {}".format(n+1, old_data[n]["item"]))
        answer = int(input("Which do you want to delete : "))
        del old_data[answer - 1]
        with open("ecommerce.json", "w") as file:
            json.dump(old_data, file, indent=4)
        print("Succesfully removed the item")
    def update_price(self):
        with open("ecommerce.json") as file:
            old_data = json.load(file)
        for n in range(0, len(old_data)):
            print("{}. {}".format(n+1, old_data[n]["item"]))
        answer = int(input("For which item do you want to update the price : "))
        print("Current price - {}".format(old_data[answer-1]["price"]))
        updated_price = int(input("Enter the new price : "))
        old_data[answer-1]["price"] = updated_price
        with open("ecommerce.json", "w") as file:
            json.dump(old_data, file, indent=4)
        print("Succesfully updated the price")
    def update_stock(self):
        with open("ecommerce.json") as file:
            old_data = json.load(file)
        for n in range(0, len(old_data)):
            print("{}. {}".format(n+1, old_data[n]["item"]))
        answer = int(input("For which item do you want to update the stock : "))
        print("Current stock - {}".format(old_data[answer-1]["availableStock"]))
        updated_stock = int(input("Enter the new stock : "))
        old_data[answer-1]["availableStock"] = updated_stock
        with open("ecommerce.json", "w") as file:
            json.dump(old_data, file, indent=4)
        print("Succesfully updated the stock") 

flag = True
new_class = Ecommerce()
while flag:
    option = int(input("Choose the option:\n1. List all the items available\n2. Add new item to the list\n3. Remove one item from the list\n4. Update the price for one item\n5. Update the stock for one item\n6. Exit\n->->->"))
    if option == 1:
        new_class.get_all_items()
    elif option == 2:
        new_class.add_item()
    elif option == 3:
        new_class.remove_item()
    elif option == 4:
        new_class.update_price()
    elif option == 5:
        new_class.update_stock()
    elif option == 6:
        flag = False