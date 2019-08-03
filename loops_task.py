items_list = []

print("Add item name, price and quantity. Enter 'done' when finished.\n")

# Adding items, price & quantity
while True:
	item = raw_input("Item (enter 'done' when finished):  ")
	
	if item == 'done':
		break

	price = input("Price:  ")
	quantity = input("Quantity:  ")

	one_item = {
	  "item": item,
	  "price": price,
	  "quantity": quantity,
	}

	items_list.append(one_item)

# Calculating total and printing receipt
print("\n~ Receipt ~\n---------------------------")

total = 0

for item in items_list:	
	i = items_list.index(item)
	item_total = items_list[i]['price'] * items_list[i]['quantity']
	print(" + {} {} KD{:.3f} ".format(items_list[i]['quantity'], items_list[i]['item'].capitalize(), item_total))
	total += item_total

print("---------------------------\n" + "Total: KD{:.3f}".format(total) + "\n")