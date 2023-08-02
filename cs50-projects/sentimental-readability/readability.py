from string import ascii_lowercase


def main():
    # Read a string from user
    s = input("Enter a string: ")
    # Number of letters
    letters = get_letters(s)
    # Number of words
    words = get_words(s)
    # Number of sentances
    sentences = get_sentences(s)
    # Coleman-Liau index (CLI)
    index = cli(letters, words, sentences)

    if index <= 1:
        # if indes is less than 1 we output "Before Grade 1"
        print("Before Grade 1")
    elif index >= 16:
        # if index is 16 or higher we output "Grade 16+"
        print("Grade 16+")
    else:
        # if grade is less than 16 and higer than 1 we output "Grade "+ index
        print(f"Grade {index}")


def get_letters(s):
    # if element is in alfabet then is a letter
    alfabet = list(ascii_lowercase)
    count = 0
    for letter in s:
        if letter.lower() in alfabet:
            count = count + 1

    return int(count)


def get_words(s):
    # we create a list with all words in the string then return lenght of list
    word_list = s.split()
    return int(len(word_list))


def get_sentences(s):
    # we check for end of a sentence ("!", ".", "?")
    count = 0
    for letter in s:
        if letter in ["!", ".", "?"]:
            count = count + 1

    return int(count)


def cli(letters, words, sentences):
    # calculates Coleman-Liau index (CLI)
    l = letters / words * 100
    s = sentences / words * 100
    return int(round(0.0588 * l - 0.296 * s - 15.8))


main()