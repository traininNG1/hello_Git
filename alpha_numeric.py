def alpha_numeric(string):
    sentence = string.split()
    output = []
    #iterating and checking each word for alphanumeric
    for i in sentence:
        if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
            output.append(i)
    return output
string = input("Enter a sentence:")
sentence = alpha_numeric(string)
print("Alpha-numeric words are:",sentence)
