class TicketBookingSystem:
    def __init__(self):
        self.tickets = {}  # Store ticket details with seat number as the key
        self.seat_count = 10  # Number of seats available for booking

    def display_menu(self):
        print("\nWelcome to the Ticket Booking System!")
        print("1. Book a Ticket")
        print("2. View Booked Tickets")
        print("3. Cancel a Ticket")
        print("4. Exit")

    def book_ticket(self):
        if len(self.tickets) >= self.seat_count:
            print("Sorry, all seats are booked.")
            return

        name = input("Enter your name: ")
        seat_number = input("Enter desired seat number (1-10): ")

        if seat_number in self.tickets:
            print("This seat is already booked. Please choose a different seat.")
        elif not seat_number.isdigit() or int(seat_number) < 1 or int(seat_number) > 10:
            print("Invalid seat number. Please enter a number between 1 and 10.")
        else:
            self.tickets[seat_number] = name
            print(f"Ticket booked successfully for {name} at seat {seat_number}.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets booked yet.")
        else:
            print("\nBooked Tickets:")
            for seat, name in sorted(self.tickets.items()):
                print(f"Seat {seat}: {name}")

    def cancel_ticket(self):
        if not self.tickets:
            print("No tickets booked to cancel.")
            return

        seat_number = input("Enter the seat number to cancel booking: ")

        if seat_number in self.tickets:
            del self.tickets[seat_number]
            print(f"Booking for seat {seat_number} has been cancelled.")
        else:
            print("No booking found for this seat.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_ticket()
            elif choice == "2":
                self.view_tickets()
            elif choice == "3":
                self.cancel_ticket()
            elif choice == "4":
                print("Exiting the system. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the ticket booking system and run it
if __name__ == "__main__":
    system = TicketBookingSystem()
    system.run()
