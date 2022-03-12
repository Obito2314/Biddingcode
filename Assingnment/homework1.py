number_of_bids = 0
count = 0
auction_fee = 0.0
item_no = 0
sold_items = 0
less_than_reserve = 0
zero_bids_items = 0
min_items = 10
while True:
    try:
        n = int(input("Enter the number of items in the auction: "))
        if n < min_items:
            raise ValueError
    except ValueError:
        print ("Number of items have to be at least 10!")
    else:
        current_highest_bid = [0.0]*n
        item_bids = [0]*n
        item_description = []*n
        reserve_price = []*n
        item_numbers = []*n
        buyer_no_Array = [0]*n
        break

#TASK 1

for i in range(n):
    item_no = item_no + 1
    item_numbers.append(item_no)
    print ("ENTER DETAILS FOR ITEM NO.", item_no)
    description = input("Enter description for item no. " + str(item_no))
    item_description.append(description)
    reserve = float(input("Enter reserve price for item no. " + str(item_no)))
    reserve_price.append(reserve)

#TASK 2

while count != "y":
    for i in range(n):
        print ("Item number:", item_numbers[i], "Description:", item_description[i], "Reserve price:", reserve_price[i], end = " ")
        print ("Current highest bid:", current_highest_bid[i], "No. of bids:", item_bids[i], end = " ") 
        print ("Buyer with highest bid:", buyer_no_Array[i])   

    choice = input("Do you want to bid for items in this auction? (y/n): ")

    if (choice == "y"):

        buyer_no = int(input("Enter your buyer ID: "))

        item_choice = int(input("Enter the item number for your choice of item: "))
        if item_choice in item_numbers:
            index = item_numbers.index(item_choice)    
            while True:
                try:
                    bid_price = float(input("Please enter your bid: "))
                    if (bid_price <= current_highest_bid[index]):
                        raise ValueError
                except ValueError:
                    print ("Bid should be higher than the current highest bid!")
                else:
                    current_highest_bid[index] = bid_price
                    number_of_bids = int(item_bids[index]) + 1
                    item_bids[index] = number_of_bids
                    print ("Bids for", item_description[index], "are:", item_bids[index])
                    buyer_no_Array[index] = buyer_no
                    break
        else: 
            print ("Invalid item code!") 
    elif (choice == "n"):
        count = input("END THE AUCTION? Enter 'n' to continue bidding or 'y' to end the auction: ")

#TASK 3

if (count == "y"):
    sold = False
    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] >= reserve_price[i]):
            sold = True
            sold_items = sold_items + 1
            auction_fee = auction_fee + (current_highest_bid[i] * 0.1)
    print ("The total auction company fee is: $", auction_fee)

    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] < reserve_price[i]):
            less_than_reserve = less_than_reserve + 1
            print ("Item code", item_numbers[i], "with final bid $", current_highest_bid[i], "has not reached the reserve price.")

    for i in range(len(current_highest_bid)):
        if (current_highest_bid[i] == 0):
            zero_bids_items = zero_bids_items + 1
            print ("Item code", item_numbers[i], "has not received any bids.")

    print ("Number of items sold are:", sold_items)
    print ("Number of items that did not meet the reserve price are:" , less_than_reserve)
    print ("Number of items with no bids are:", zero_bids_items)
else:
    print ("Invalid input!")