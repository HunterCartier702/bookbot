from stats import get_book_text, get_book_cc, get_book_wc, sort_count


def main():
	file_path = "books/frankenstein.txt"
	text = get_book_text(file_path)
	word_count = get_book_wc(text)
	print(word_count)
	
	chars = get_book_cc(text)
	print(chars)

	x = sort_count(chars)
	print(x)

if __name__ == '__main__':
	main()
