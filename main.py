from pprint import pprint
def main():
    # function to open the file and get the contents
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)

    # First line of the report
    print(f"--- Begin report of {book_path} ---\n")

    # count all the words in book_text
    total_num_words = count_words(book_text)
    print(f"This book has {total_num_words} total words\n")

    # Take the text from the book as a string (book_text) and return
    # a dictionary with the number of times each character appears in the string.
    char_dictionary = count_characters(book_text)

    # Conver the char_dictionary into a list of dictionaries, where each dictionary has
    # as key the letter, and its value the number of times they occur, e.g. {'letter': 'p', 'num': 6121}
    list_of_char_dictionaries = convert_dict_to_list(char_dictionary)
    # Sort the dictionaries by the total number of occurrences from largest to smallest
    list_of_char_dictionaries.sort(reverse=True, key=sort_on)

    # Produce the report that itemises how many times each character was found
    print_character_report(list_of_char_dictionaries)

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

def convert_dict_to_list(dictionary):
    result = [{'letter': k, 'num': v} for k, v in dictionary.items() if k.isalpha()]
    return result

def print_character_report(list_of_dicts):
    for dict in list_of_dicts:
        print(f"The '{dict['letter']}' character was found {dict['num']} times")

def sort_on(dictionary):
    return dictionary['num']

if __name__ == "__main__":
    main()