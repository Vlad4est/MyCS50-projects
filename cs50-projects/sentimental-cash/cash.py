
def main():
    cents = get_cents()
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1
    coins = quarters + dimes + nickels + pennies
    print(coins)

# get cents from user


def get_cents():
    while True:
        try:
            cents = float(input("Enter cents amount: "))
        except:
            continue
            # while cents is negative or not a number get user input
        if cents > 0:
            return cents/0.01

# calculate quarters by dividing cents with 25


def calculate_quarters(cents):
    return int(cents/25)

# calculate dimes by dividing cents with 10


def calculate_dimes(cents):
    return int(cents/10)

# calculate nickels by dividing cents with 5


def calculate_nickels(cents):
    return int(cents/5)

# return number of pennies


def calculate_pennies(cents):
    return int(cents)

# call main function


main()