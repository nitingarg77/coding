# python Banking Program

balance = 0.0


def show_balance():
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = input("Enter amount to deposit: $")    
    try:
        amount = float(amount)
        if amount <= 0:
            print("Please enter a positive amount.")
            return 0
        else:
            global balance
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")            


def withdraw():
    amount = input("Enter amount to withdraw: $")  
    global balance
    try:
        amount = float(amount)
        if amount <= 0:
            print("Please enter a positive amount.")
            return 0
        elif amount > balance:
            print("Insufficient funds.")
            return 0
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def main():
    balance = 0
    is_running = True
    while is_running:
        print("\nWelcome to the Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
        choice = input("Choose an option (1-4): ")
    
        if choice == '1':
          show_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            is_running = False
            print("Thank you for using the Banking Program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")     


if __name__ == "__main__":
    main()