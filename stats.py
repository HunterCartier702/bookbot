# read text of book
def get_book_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		file_contents = f.read()
	return file_contents


# get word count of book
def get_book_wc(text):
	word_count = 0
	words = text.split()
	for word in words:
		word_count += 1
	return f"{word_count} words found in the document"


# get character count of book
def get_book_cc(text):
	text = text.lower()
	char_count = {}
	for char in text:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count