def spin_row():
    symbols = ['A', 'B', 'C', 'D', 'E']

    result = []
    for symbol in range(3):
        import random
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        return bet * 10
    return 0

def main():
    balance = 100
    print("Welcome to the Slot Machine!")
    print(f"You start with a balance of ${balance}.")
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = int(input("Enter your bet amount (or 0 to quit): "))

       
        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue

        if bet == 0:
            print("Thanks for playing!")
            break

        #balance -= bet
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout - bet
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("No win this time.")




if __name__ == "__main__":
    main()
