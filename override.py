class Restaurant:
    def opening_hours(self):
        return "opening hours depend upon the demand"

class FastFood_Rest(Restaurant):
    def opening_hours(self):
        return "opens at 9:00 AM and closes at 12:00 AM"

class dining_rest(Restaurant):
    def opening_hours(self):
        return  "opens at 11:00 AM and closes at 12:30 AM"
    
a = FastFood_Rest()
b = dining_rest()
print("Timing for Fast food Restaurant:", a.opening_hours())
print("Timing for Dining :",b.opening_hours())

        
