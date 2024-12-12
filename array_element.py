def array_element(array,output):
    for i in range(len(array)):
        if array[i]==output:
            print("The element ",output, " found at index ",i)
            return
    else:
        print("Element ",output, "not present in the array")
#predefined array
array = [10,20,30,5,7,32,45,60,70,80,90,100,85,65,12,46,79]
output= int(input("Enter the element to search for:"))
array_element(array,output)
