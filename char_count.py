def char_count(input):
    count={}
    for i in input.replace(" ",""):
        if i in count:
            count[i]=count[i]+1
        else:
            count[i] = 1
    return count
input = input("Enter the string:")
result=char_count(input)
print("Character occurence :",result)
