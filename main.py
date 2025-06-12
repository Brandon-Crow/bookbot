from stats import dict_to_list, get_num_words, count_character, sort_char
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
    
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

filepath= sys.argv[1]
bookstring = (get_book_text(filepath))
bookwordcount = get_num_words(bookstring)
charactercount = count_character(bookstring)

char_counts_list = dict_to_list(charactercount)
sorted_counts = sort_char(char_counts_list)

print(f'============ BOOKBOT ============')
print(f'Analyzing book found at {filepath}...')
print("----------- Word Count ----------")
print (f'Found {bookwordcount} total words')
print("--------- Character Count -------")
for item in sorted_counts:
    print(f"{item['char']}: {item['num']}")
