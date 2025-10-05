from collections import Counter


def getbooktext(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# def main():
#     path = '/home/johnb/bookbot/bookbot/books/frankenstein.txt'
#     book_text = getbooktext(path)
#     print(book_text)

# main()

def countwords(text: str) -> str:
    num_words = len(text.split())
    return f"Found {num_words} total words"

# def main():
#     path = '/home/johnb/bookbot/bookbot/books/frankenstein.txt'
#     book_text = getbooktext(path)
#     print(countwords())

# main()

def countcharacters(text: str) -> dict:
    text = text.lower()
    return dict(Counter(text))
    

def get_char(item):
    return item["num"]

def sort_character_list(countcharacters: dict) -> list:
    sorted_list = []
    for char, count in countcharacters.items():
        if char.isalpha():  
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=get_char, reverse=True)
    return sorted_list