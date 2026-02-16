##A movie ticket booking system:
def calculate_final_price(base_price, age, seat_type, show_time, is_member, is_weekend):
    
    # Eligibility Check:
    if age < 18:
        print("❌ You must be at least 18 to book a ticket.")
        return None

    # Evening show restriction:
    if show_time == "Evening" and age < 21 and not is_member:
        print("❌ Evening shows are only for 21+ or members.")
        return None

    print("✅ Ticket booking condition satisfied")

    # Discount:
    discount = 3 if is_member and age >= 21 else 0

    # Extra Charges:
    extra_charges = 2 if is_weekend or show_time == "Evening" else 0

    # Service Charges:
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1

    # Final Price Calculation:
    final_price = base_price + extra_charges + service_charges - discount

    return final_price


def main():
    base_price = 15

    while True:
        try:
            age = int(input("Enter your age: "))
            seat_type = input("Enter seat type (Premium/Gold/Regular): ").title()
            show_time = input("Enter show time (Morning/Evening): ").title()
            is_member = input("Are you a member? (yes/no): ").lower() == "yes"
            is_weekend = input("Is it weekend? (yes/no): ").lower() == "yes"

            final_price = calculate_final_price(
                base_price, age, seat_type, show_time, is_member, is_weekend
            )

            if final_price is not None:
                print(f"🎟 Final price of ticket: ${final_price}")

        except ValueError:
            print("⚠ Please enter valid numeric age.")

        again = input("\nDo you want to book another ticket? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using Movie Ticket Booking System 🎬")
            break


if __name__ == "__main__":
    main()

