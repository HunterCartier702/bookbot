

def get_book_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		file_contents = f.read()
	return file_contents


def main():
	path = get_book_text("books/frankenstein.txt")
	return path


print(main())