def get_book_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		file_contents = f.read()
	return file_contents

def get_book_wc():
	word_count = 0
	wc = get_book_text("books/frankenstein.txt")
	words = wc.split()
	for word in words:
		word_count += 1
	return f"{word_count} words found in the document"