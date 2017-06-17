import operator
import csv

inv = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


# Displays the inventory.
def display_inventory(inventory):
    total = 0
    print("Inventory: ")
    for keys, values in inventory.items():
        print(values, keys)
        total += values

    print("Total number of items: %d" % total)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for i in range(len(added_items)):
        for j in list(inventory):
            if added_items[i] == j:
                inventory[j] += 1
        if added_items[i] not in list(inventory):
            inventory[added_items[i]] = 1

    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    # Inventory sorted by values in an ascending order,
    # then by reversing it making a list with descending order.
    inventory_asc = sorted(inventory.items(), key=operator.itemgetter(1))
    inventory_desc = reversed(inventory_asc)

    # Separate lists for keys and values for later use.
    keys = inventory.keys()
    values = inventory.values()
    keylist = list(keys)
    valuelist = list(values)
    pairlist = []

    total = 0

    # Length of the longest key and value in the list,
    # which helps us to determine row length in the table.
    key_length = len(max(keylist, key=len))
    value_length = len(str(max(valuelist)))

    # Calculates the total number of items.
    for keys, values in inventory.items():
        total += values

    # This makes sure that the columns are idented properly,
    # even if the longest value is shorter than 5 digits (length of "count")
    # and the longest key is shorter than 9 letters (length of "item name")
    if key_length < 9:
        key_length = 9
    if value_length < 5:
        value_length = 5

    for a, b in zip(keylist, valuelist):
        pairlist.extend([[b, a]])

    # Table creation
    print("Inventory:\n",
          " "*(value_length - 5) + "count",
          " "*(key_length - 8) + "item name\n",
          "-"*(key_length + value_length + 3))

    if order == "count,asc":
        for item in inventory_asc:
            print(" "*(value_length - len(str(item[1]))), item[1],
                  " "*(key_length - len(str(item[0]))), item[0])

    elif order == "count,desc":
        for item in inventory_desc:
            print(" "*(value_length - len(str(item[1]))), item[1],
                  " "*(key_length - len(str(item[0]))), item[0])

    elif order is None:
        for item in pairlist:
            print(" "*(value_length - len(str(item[0]))), item[0],
                  " "*(key_length - len(str(item[1]))), item[1])

    else:
        raise ValueError("Invalid parameter for order")

    print("-"*(key_length + value_length + 3), "\n",
          "Total number of items: %d " % total)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    path = '/home/akos/codeLUL/git/%s' % filename
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE, escapechar="|")
        data = [row for row in reader]
        data_length = len(data)
        item = [item for item in data[data_length - 1]]

    for row in range(data_length):
        for column in range(len(item)):
            for j in list(inventory):
                if data[row][column] == j:
                    inventory[j] += 1
            if data[row][column] not in list(inventory):
                inventory[data[row][column]] = 1

    return inventory

# Test block for the import_inventory function:
# import_inventory(inv, "import_inventory.csv")
# print_table(inv, "count,asc")


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    # A list that contains each value the amount of times
    # they occur in our inventory.
    invlist = []

    for key, value in inventory.items():
        invlist.extend([key] * value)

    path = '/home/akos/codeLUL/git/%s' % filename
    with open(path, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE, escapechar="|")
        writer.writerow(invlist)


def main():
    print("Display inventory function: ")
    display_inventory(inv)

    print("\nAdd to inventory function demonstrated with the following loot:\n"
          "dragon_loot = [gold coin, dagger, gold coin, gold coin, ruby]")
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)

    print("\nPutting the inventory into a well organized table with the\n"
          "print_table function first in an ascending than in a descending order: ")
    print_table(inv, "count,asc")
    print_table(inv, "count,desc")

    print("\nImporting the following list from import_inventory.csv:\n"
          "[ruby, rope, ruby, gold coin, ruby, axe]")
    import_inventory(inv, "import_inventory.csv")
    print_table(inv, "count,asc")

    print("\nFinally exporting this inventory to export_inventory.csv.\n"
          "You can find the file in the following directory:\n"
          "/home/akos/codeLUL/git")
    export_inventory(inv, "export_inventory.csv")


main()
