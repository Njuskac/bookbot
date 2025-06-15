import sys

from stats import get_num_words

from stats import count_characters

from stats import sorting

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    count = count_characters(text)
    sorted_chars = sorting(count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")

if __name__ == "__main__":
    main()
