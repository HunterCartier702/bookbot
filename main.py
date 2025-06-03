from stats import get_book_text, get_book_cc, get_book_wc


def main():
	text = get_book_text("books/frankenstein.txt")
	word_count = get_book_wc(text)
	print(word_count)
	
	chars = get_book_cc(text)
	print(chars)
	# for key, value in chars.items():
	# 	print(f"{key}: {value}")

	

if __name__ == '__main__':
	main()
# print(main())