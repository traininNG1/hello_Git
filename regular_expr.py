import re

def regular_exprs(string, remove):
    
    result = re.sub(rf'\b{remove}\b', ' ', string)
    result = re.sub(r'\s+', ' ', result).strip()
    return result
# Input from user
string = input("Enter the string: ")
remove = input("Enter the word to remove: ")
#fn call
updated_string = regular_exprs(string, remove)
print("Updated string:", updated_string)



