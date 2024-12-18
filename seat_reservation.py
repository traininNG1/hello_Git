import threading

total_seat = 50

def reserve_seat(id):
    global total_seat

    seat_request = int(input(f"{id},How many seats you would like to book? :"))
    
    if seat_request <= total_seat:
        total_seat -= seat_request
        print(f"Passenger {id}:with {seat_request} seat(s) Booking Successfull!..Seat Left : {total_seat}")
    else:
        print(f"Passenger {id} Booking Failed..Not enough seats. seat left : {total_seat}")


def main():
    global total_seat

    print(f"welcome to Bus reservation...Total seats available :{total_seat}")
    num = int(input("Number of users:"))

    threads =[]
    for id in range(1,num+1):
        a = threading.Thread(target=user_thread,args=(id,))
        threads.append(a)
        a.start()

    for a in threads:
        a.join()

    print("Booking completed")
if __name__ == "__main__":
    main()
