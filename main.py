def main():
    book_path = 'books/frankenstein.txt'
    book_content = get_book_text(book_path)
    # book_word_count = count_words(book_content)
    # char_count = count_letters(book_content)
    print_report(book_content, book_path)

def sort_by(dict):
    return dict["num"]

def get_book_text(path: str):
    with open(path) as f:
        return f.read()

def count_words(text: str):
    words = text.lower().split()
    return len(words)        

def count_book_letters_dict(text: str):
    content = text.lower()
    dict = {}
    range = 'abcdefghijklmnopqrstuvwxyz'
    for letter in range:
        dict[letter] = count_letters(content, letter)
    return dict

def count_book_letters_list(text: str):
    content = text.lower()
    list = []
    range = 'abcdefghijklmnopqrstuvwxyz'
    for letter in range:
        dict = {}
        dict["name"] = letter
        dict["num"] = count_letters(content, letter)
        list.append(dict)
    return list

def print_report(text: str, path: str):
    print(f'--- Begin report of {path} ---')
    word_count = count_words(text)
    print(f'{word_count} words found in the document')
    print()

    letter_count_list = count_book_letters_list(text)
    letter_count_list.sort(reverse=True, key=sort_by)

    for dict in letter_count_list:
        print(f'The \'{dict["name"]}\' character was found {dict["num"]} times')

    print('--- End report --')

def count_letters(text: str, letter: str):
    content = text
    count = 0
    for char in content:
        if char == letter:
            count +=1
    return count

main()