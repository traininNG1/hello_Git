
class Menu_Management:
    def __init__(self):
        self.menu={}
    def add_item(self,item,price):
        self.menu[item] = price
        print(f"Added {item} to the menu, Price of {item} is :{price}")

    def display_items(self):
        print("Menu:")
        for item,price in self.menu.items():
            print(f"{item} : {price}")


class staffManagement():
    def __init__(self):
        self.staff_list = {}

    def add_staff(self,name,designation):
        self.staff_list[name]=designation
        print(f"Added staff Name: {name}, Role:{designation}")
    
    def view_staff(self):
       
        for name,designation in self.staff_list.items():
            print(f"{name} : {designation}")

class Restuarant(Menu_Management,staffManagement):
    def __init__(self):
        Menu_Management.__init__(self)
        staffManagement.__init__(self)


    def show_details(self):
       
        
        self.display_items()  # Call the instance method on `self`
        print("Staff List:")
        self.view_staff()
        
rest_a = Restuarant()    

rest_a.add_staff("FARIZ","accontant")
rest_a.add_staff("bubbu","manager")
rest_a.add_staff("Ram","waiter")
rest_a.add_item("Pizza","$22.55")
rest_a.add_item("pasta","$33.33")
rest_a.show_details()