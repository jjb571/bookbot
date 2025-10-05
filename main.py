from stats import countwords, getbooktext, countcharacters, sort_character_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = getbooktext(path)

    # Word count
    print(countwords(text))

    # Character counts
    char_counts = countcharacters(text)
    print(char_counts)

    sorted_chars = sort_character_list(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()





