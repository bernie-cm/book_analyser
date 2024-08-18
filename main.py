def main():
    # function to open the file and get the contents
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    # print the text
    print(book_text)

def get_book_contents(path):
    with open(path) as fin:
        return fin.read()
    

if __name__ == "__main__":
    main()