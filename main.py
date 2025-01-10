def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count = count_char(text)
    report(char_count)
    print("--- End report ---")



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

def report(sorted_dict):
    list_of_dict = []
    for char, count in sorted_dict.items():  
        if char.isalpha():
            new_dict = {"name": char, "num": count}
            list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)

    for item in list_of_dict:
        print(f"The '{item['name']}' character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]

main()
