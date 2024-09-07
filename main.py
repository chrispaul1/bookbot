def return_book(book_path):
	with open(book_path) as f:
		file_contents = f.read()
	return file_contents

def count_words(book_text):
	words = book_text.split()
	return len(words)

def count_char(book_text):
	lowered_book_text = book_text.lower()
	char_count_dict = {}
	for i in range(0,len(lowered_book_text)):
		if lowered_book_text[i] in char_count_dict:
			char_count_dict[lowered_book_text[i]] += 1
		else:
			char_count_dict[lowered_book_text[i]] = 1
	return char_count_dict

def convert_dict(dict):
  dict_list = []
  for key, val in dict.items():
	  dict_list.append({"char":key,"num":val})
  return dict_list
		
def sort_on(dict):
	return dict["num"]

def display_char_count(list):
	for ele in list:
		char = ele["char"]
		count = ele["num"]
		if(char.isalpha()):
		  print(f"The '{char}' character was found {count} times")


def main():
	book_text = return_book("books/frankenstein.txt")
	book_words_len = count_words(book_text)
	book_char_dict = 	count_char(book_text)
	char_count_list = convert_dict(book_char_dict)
	char_count_list.sort(reverse=True,key=sort_on)
	print(book_text)
	#print(book_char_dict)
	print(f"\nThere are {book_words_len} words in the book\n")
	display_char_count(char_count_list)
	
main()
