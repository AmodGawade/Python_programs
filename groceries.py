#!/Users/amod/venv/bin/python

# Author name : Amod gawade
# Date : 20 march 2020

# Asking input from user
item_num = int(input("Please enter the number of items on your grocery  list."))
item_list = [str(input("What is the item #" + str(count + 1) + " on your list?\n")) for count in range(item_num)]
item_price = sum(int(input("Enter the price of the item \n")) for i in range(item_num))
item_quantity = sum(int(input("What is the quantity of item #" + str(count + 1) + " that you bought?\n")) for count in
                    range(item_num))

# calculating total
total = sum(int(item_price * item_quantity)for x in range(item_num))
print("The total is...")
print(total)
