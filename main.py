# main_project.ipynb

from car_rental import CarRental, Customer

def main():
    car_rental = CarRental(100)  # Initializing with 100 cars
    customer = Customer()

    while True:
        print("""
        ====== Car Rental Shop =======
        1. Display available cars
        2. Request a car on hourly basis ₹500/hour
        3. Request a car on daily basis ₹1000/day
        4. Request a car on weekly basis ₹5000/week
        5. Return a car
        6. Exit
        """)
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            car_rental.display_available_cars()
        
        elif choice == 2:
            customer.request_car()
            rental_time = car_rental.rent_car_on_hourly_basis(customer.cars)
            if rental_time:
                customer.rentalTime = rental_time
                customer.rentalBasis = 1  # hourly
        
        elif choice == 3:
            customer.request_car()
            rental_time = car_rental.rent_car_on_daily_basis(customer.cars)
            if rental_time:
                customer.rentalTime = rental_time
                customer.rentalBasis = 2  # daily
        
        elif choice == 4:
            customer.request_car()
            rental_time = car_rental.rent_car_on_weekly_basis(customer.cars)
            if rental_time:
                customer.rentalTime = rental_time
                customer.rentalBasis = 3  # weekly
        
        elif choice == 5:
            request = customer.return_car()
            bill = car_rental.return_car(request)
            customer.rentalBasis, customer.rentalTime, customer.cars = 0, 0, 0
        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()