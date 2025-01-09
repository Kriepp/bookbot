def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # dict_to_list = list(count_char(text))
    # dict_sorted = dict_to_list.sort(reverse=True, key=sort_on)
    print(f"{num_words} words found in the document")
    # print_report = report(dict_sorted)
    count_char(num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(text):
    lower_text = text.lower()
    count = []
    for c in lower_text:
        if c in count:
            count["c"]['name'] += 1
        else:
            count["c"]['name'] = 1
    print(f"{count}")
    return count

def sort_on(dict):
    return dict["num"]

#! Create a dictionary of dictionaries
def report(sorted_dict):
    for c in sorted_dict:
        if c.isalpha():
            print(f"{c} Is alpha")   
            

main()
