import threading

class Num_of_seats:
    def __init__(self, total_seat):
        self.total_seat = total_seat
        self.lock = threading.Lock()

    def reserve_seat(self, passenger_id):
        seat_request = int(input(f"Passenger {passenger_id}: How many seats would you like to book? "))

        # Locking the critical section
        self.lock.acquire()
        try:
            if seat_request <= self.total_seat:
                self.total_seat -= seat_request
                print(f"Passenger {passenger_id}: {seat_request} seat(s) booking successful! Seats left: {self.total_seat}")
            else:
                print(f"Passenger {passenger_id}: Booking failed. Not enough seats. Seats left: {self.total_seat}")
        finally:
            self.lock.release()

def main():
    total_seat = 50
    reservation_ssm = Num_of_seats(total_seat)

    print(f"Welcome to Bus Reservation System. Total seats available: {total_seat}")
    num = int(input("Number of users: "))

    threads = []
    for passenger_id in range(1, num + 1):
        a = threading.Thread(target=reservation_ssm.reserve_seat, args=(passenger_id,))
        threads.append(a)
        a.start()

    for a in threads:
        a.join()

    print("All bookings completed.")

if __name__ == "__main__":
    main()
