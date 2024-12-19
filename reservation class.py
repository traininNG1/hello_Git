import threading

class Num_of_seats:
    def __init__(self,total_seat):
        self.total_seat = total_seat
        self.lock = threading.Lock()

    def reserve_seat(self,id):
        seat_request = int(input(f"Passenger {id}: How many seat would you like to book."))

        #locking the critical section
        self.lock.acquire()
        try:
            if seat_request <= self.total_seat:
                self.total_seat -= seat_request
                print(f"Passenger {id}:with {seat_request} seat(s) Booking Successfull!..Seat Left : {self.total_seat}")
            else:
                print(f"Passenger {id} Booking Failed..Not enough seats. seat left : {self.total_seat}")
        finally:
            self.lock.release()

def main():
        total_seat = 50
        reservation_ssm = Num_of_seats(total_seat)

        print(f"welcome to Bus reservation...Total seats available :{total_seat}")
        num = int(input("Number of users:"))

        threads =[]
        for id in range(1,num+1):
            a = threading.Thread(target=reservation_ssm.reserve_seat,args=(id,))
            threads.append(a)
            a.start()

        for a in threads:
            a.join()

        print("All bokings completed")

if __name__== "__main__":
    main()