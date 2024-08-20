def main():
    # function to open the file and get the contents
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    # count all the words in book_text
    total_num_words = count_words(book_text)
    print(f"This book has {total_num_words} total words.")

    # Take the text from the book as a string (book_text) and return
    # a dictionary with the number of times each character appears in the string.
    char_dictionary = count_characters(book_text)
    print("Here is the character count")
    print(char_dictionary)


def get_book_contents(path):
    with open(path) as fin:
        return fin.read()
    
def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(book_text):
    # List comprehension to ensure all the words are lower case
    words = [word.lower() for word in book_text.split()]

    # Init an empty dictionary to capture all the letters and their number of occurrences
    result = {}
    for word in words:
        for char in word:
            if char in result:
                result[char] += 1   # The character already exists so increase count by 1
            else:
                result[char] = 1    # The character does not exist so init the count with 1
    return result


if __name__ == "__main__":
    main()