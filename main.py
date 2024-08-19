def main():
    # function to open the file and get the contents
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    # count all the words in book_text
    total_words = count_words(book_text)
    print(total_words)

def get_book_contents(path):
    with open(path) as fin:
        return fin.read()
    
def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)
    

if __name__ == "__main__":
    main()