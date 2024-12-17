import datetime

def placeOrder_decorator(func):
    def sub_placeorder(item_name,num_item):
        print("Placed order at :",datetime.datetime.now())
        func(item_name,num_item)
    
    return sub_placeorder

@placeOrder_decorator
def place_order(item_name,num_item):
    print(f"Item : {item_name}")
    print(f"Quantity:{num_item}")

place_order("pen",30)

