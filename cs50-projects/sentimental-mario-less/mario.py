
def printRow(n, a):
    # recursive function to print n rows
    if (n != 0):
        printRow(n-1, a)
        print(" " * (a - n), end="")
        print("#" * n, end="")
        print()


def main():
    # make sure users imputs an intiger from 1 to 8
    while True:
        try:
            n = int(input("n: "))
        except:
            continue

        if (n > 0 and n < 9):
            break
    a = n
    printRow(n, a)
    # call functoon printRow


# call main funtion
main()