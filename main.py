def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_char(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(text):
    lower_text = text.lower()
    count = {}
    for c in lower_text:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_on(dict):
    return dict["num"]

def report(sorted_dict):
    for c in sorted_dict:
        if c.isalpha():
            

main()
