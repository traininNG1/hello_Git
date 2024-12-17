from datetime import datetime

def myDecorator(func):
    def place_order(*args, **kwargs):  # Use args and **kwargs to accept any number of arguments
        print("Order placed on", datetime.now())
        return func(*args, **kwargs)  # Pass the arguments to the original function
    return place_order

@myDecorator
def order(item_name, number_of_items):
    print(f"{item_name} is purchased in {number_of_items} quantity")

# Calling the function with arguments
order("shoe", 2)
