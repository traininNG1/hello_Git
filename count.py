def countOccurence(str):
    uniqueChar=""
    for i in str.replace(" ",""):
        if i not in uniqueChar:
            uniqueChar+=i
            print(i,":",str.count(i))
input=input("Enter the word to count the character:- ")
countOccurence(input)


