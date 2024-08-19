def main():
    # function to open the file and get the contents
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    # count all the words in book_text
    total_words = count_words(book_text)
    print(f"This book has {total_words} total words.")

    '''Add a new function to your script that takes the text from the book as a string, 
    and returns the number of times each character appears in the string. 
    Convert any character to lowercase, we don't want duplicates.'''
    char_dictionary = count_characters(total_words)
    print("Here is the character count")
    print(char_dictionary)


def get_book_contents(path):
    with open(path) as fin:
        return fin.read()
    
def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_character(list_of_words):
    result = {}
    for word in list_of_words:
        for char in word:
            if char.lower() in result:
                result[char] += 1   # The character already exists so increase count by 1
            else:
                result[char] = 1    # The character does not exist so init the count with 1
    return result

if __name__ == "__main__":
    main()