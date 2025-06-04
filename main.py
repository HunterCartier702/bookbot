import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

# Books taken from: https://www.gutenberg.org/ 
# https://www.gutenberg.org/cache/epub/41445/pg41445.txt


def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text(book_path) # grab all text
	num_words = get_num_words(text) # grab word count
	chars_dict = get_chars_dict(text) # grab '{char: count}'
	chars_sorted_list = chars_dict_to_sorted_list(chars_dict) #dict to list.sort
	print_report(book_path, num_words, chars_sorted_list)



def get_book_text(path):
    with open(path) as f:
        return f.read()



def print_report(book_path, num_words, chars_sorted_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")





if __name__ == '__main__':
	main()
