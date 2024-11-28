from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    """Drive the currently selected taxi and update the total bill."""
    if current_taxi:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        distance_driven = current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def choose_taxi(current_taxi, taxis):
    """Display available taxis and allow the user to choose one."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Display all taxis in a formatted list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
