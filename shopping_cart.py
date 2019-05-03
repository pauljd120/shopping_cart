# shopping_cart.py


import datetime

def to_usd(num):
    dollar_num = "${0:.2f}".format(num)
    return dollar_num

def find_product(each, products, running_total):
    matching_products = [p for p in products if str(p["id"]) == str(each)]
    matching_product = matching_products[0]
    running_total = running_total + matching_product["price"]
    number_to_print = to_usd(matching_product["price"])
    print("+ " + matching_product["name"] + " " + str(number_to_print))
    return running_total


if __name__ == "__main__":
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

    running_total = 0

    itemsOrdered = []

    while True:
        selected_id = input("Please input a product identifier, or DONE if there are no more items: ")
        if selected_id == "DONE":
            break
        else:
            itemsOrdered.append(selected_id)

    print("---------------------------------")
    print("MUCH GOOD GROCERY")
    print("WWW.MUCHGOODVERYNICE.COM")
    print("---------------------------------")
    current_time = datetime.datetime.now()
    print("CHECKOUT AT: " + current_time.strftime("%x") + " " + current_time.strftime("%X") + " " + current_time.strftime("%p"))
    print("---------------------------------")
    print("SELECTED PRODUCTS:")
    for each in itemsOrdered:
        running_total = find_product(each, products, running_total)
    print("---------------------------------")


    tax = running_total * .06
    total = running_total + tax


    running_total = to_usd(running_total)
    tax = to_usd(tax)
    total = to_usd(total)


    print("SUBTOTAL: ", running_total)
    print("TAX: " + str(tax))
    print("TOTAL: " + str(total))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")
