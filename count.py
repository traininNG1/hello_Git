def countOccurence(string):
    for i in string:
        print(i,"-",string.count(i))
    print("count is",string.count("l"))
string = input("Enter the string:")
result=countOccurence(string)
