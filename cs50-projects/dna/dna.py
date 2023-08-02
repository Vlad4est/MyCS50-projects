import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit()


    database = []
    with open(sys.argv[1], "r") as csv_file:
        csv_reader_db = csv.DictReader(csv_file)
        for line in csv_reader_db:
            database.append(line)
    # print(database)


    with open(sys.argv[2], "r") as dna_file:
        dna_seq = dna_file.read()



    # get STR for first line except the "name"
    subseq = list(database[0].keys())[1:]
    strs = dict()
    for i in subseq:
        strs[i] = longest_match(dna_seq , i)



    for line in database:
        count = 0
        for i in subseq:
            if int(line[i]) == strs[i]:
                count = count + 1

        if len(subseq) == count:
            print(line["name"])
            sys.exit()

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
