def sandwich_order(filling):
    menu = {
        "egg" : 50.00,
        "chicken" : 60.00,
        "veg" : 45.00,
        "tuna" : 55.00,
        "bbq" : 60.00

    }
    if filling in menu:
        print(f"The price of {filling} sandwich is  ${menu[filling]}:")
    else:
        print(f"Soryy!,we don't have {filling} sandwich on our menu")
order = input("Enter the filling for your sandwich:")
sandwich_order(order)