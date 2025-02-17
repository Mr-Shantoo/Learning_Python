import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_Value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Add line number to winning lines
    return winnings, winning_lines





def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate( columns):
            if i!=len(columns)-1:

                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
        


def deposite():
    while True:
        amount = input("what  would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amoun must be greater than 0")
        else:
            print("please enter a number")
    return amount


def get_Number_Of_Lines():
    while True:
        Lines = input(
            "Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= MAX_LINES:
                break
            else:
                print("Enter a valid numbers of Lines")
        else:
            print("please enter a number")
    return Lines


def get_bet():
    while True:
        amount = input("what  would you like to bet on each Lines? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amoun must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("please enter a number")
    return amount


def spin(balance):
    Lines = get_Number_Of_Lines()
    while True:
        bet = get_bet()
        total_bet = bet * Lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {Lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, Lines, bet, symbol_Value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on line(s): {', '.join(map(str, winning_lines))}")  # Display line numbers
    else:
        print("You did not win on any line.")
    return winnings - total_bet

def main():
    balance = deposite()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()

