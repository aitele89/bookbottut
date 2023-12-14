def main():
    book_path = "books/frankenstein.txt"
    text = read_a_book(book_path)
    word_count = word_num(text)
    letter_dict = word_search(text)
    print(f"--- Book Report For {book_path} ---")
    print(f"{word_count} words were found in the document.")
    print(" ")
    for i in letter_dict:
        count = letter_dict[i]
        if i.isalpha():
            print(f"The {i} character was found {count} times.")
    print("--- End Report ---")

def word_num(text):
    words = text.split()
    return len(words)

def read_a_book(path):
    with open(path) as f:
        return f.read()
    
def word_search(text):
    letter_dict = {}
    for letters in text:
        lowered = letters.lower()
        if lowered in letter_dict:
            letter_dict[lowered] += 1
        else:
            letter_dict[lowered] = 1
    return letter_dict

main()