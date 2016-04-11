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

def main():

    print("\t Items for Hire - by Shankar Ramesh  Vasudev")
    MENU = "Menu: \n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new items to stock\n(Q)uit"
    items = load_item()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            list_all_item(items)
        if choice == 'H':
            hire_an_item(items)
        print(MENU)
        choice = input(">>> ").upper()
        #  save_item()
    print("Farewell Message")  # change it - just for reference


def load_item():
    file = open('items.csv')
    items = []
    for line in file:
        item_in_list = line.strip().split(',')
        item_in_list[2] = float(item_in_list[2])
        items.append(item_in_list)
    file.close()
    return items


def list_all_item(items):
    print("All items on file ( '*' indicates item is currently out):")
    for number in range(len(items)):

        item_name = items[number][0]
        item_desc = items[number][1]
        item_cost = items[number][2]
        item_position = items[number][3]
        if item_position == 'out':
             item_sign = "*"
        else:
            item_sign = ""

        print("{} - {:20} {:30} = $ {:>4.2f} {}".format(number, item_name, '('+item_desc+')', item_cost, item_sign))

# load_all_item()


def hire_an_item(items):


main()
