def odd_even(num):
    d1_even=0
    d2_odd=0
    list_odd=[]
    list_even=[]
    for i in num:
        if(i%2==0):
            list_even.append(i)
            d1_even+=1
        else:
            list_odd.append(i)
            d2_odd+=1   
    print("Total even numbers=",d1_even)
    print("The even numbers are:",list_odd)
    print("Total odd numbers=",d2_odd)
    print("The odd numbers are:",list_even)
num = [12,34,56,7,8,78,90,11,33,45,67,87,1,3,5,7,9,2,4,6,8]
odd_even(num)



