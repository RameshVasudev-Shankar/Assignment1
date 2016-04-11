# '''
# CP5632 Assignment 1 2016
# Items for Hire
# Shankar Ramesh V - 3rd April 2016
#
# Pseudocode:
#
# function main():
#
#     display Welcome Message
#     display list of items loaded from file
#     display menu
#     choice
#     while choice not Q
#         if choice = L
#             function list_all_items()
#         elif choice = H
#             function hire_an_item()
#         elif choice = R
#             function return_an_item()
#         elif choice = 'A'
#             function add_item()
#         else:
#             Display Invalid Menu Message
#         display Menu
#         choice
#     display Farewell message
#
# '''
#
#
# def main():
#
#     print("\t Items for Hire - by Shankar Ramesh  Vasudev")
#     MENU = "\t Menu: \n\t (L)ist all items \n\t (H)ire an item\n\t (Return) an item\n\t (A)dd new items to stock\n\t (Q)uit"
#     print(MENU)
#     choice = input(">>> ").upper()
#     while choice != 'Q':
#         if choice == 'L':
#             list_all_item()
#         elif choice == 'H':
#             hire_an_item()
#         elif choice == 'R':
#             return_an_item()
#         elif choice == 'A':
#             add_item()
#         else:
#             print("Invalid menu choice")
#         print(MENU)
#         choice = input(">>> ").upper()
#     print("Farewell Message") #change it - just for reference
#

def load_all_item():
    print("All items on file ( '*' indicates item is currently out):")
    file = open('items.csv') #reading the csv file
    file_read = file.readlines() # reading all the lines of the csv file one by one
    for line in range(len(file_read)):
        item_in_list = file_read[line].split(',')
        item_name = item_in_list[0]
        item_desc = item_in_list[1]
        item_cost = item_in_list[2]
        item_position = item_in_list[3].rstrip()
        if item_position == 'out':
            item_sign = "*"
        else:
            item_sign = ""
        print("{} - {} ({}) = $ {} {}".format(line, item_name, item_desc, item_cost, item_sign))
    file.close()
load_all_item()

def hire_an_item():
    

