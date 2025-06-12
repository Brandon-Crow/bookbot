def get_num_words(bookstring):
    word_count=len(bookstring.split())
    #print (f'{word_count} words found in the document')
    return word_count

def count_character(bookstring: str):
    char_counts={}
    characters = bookstring.lower()
    for each in characters:
        if each.isalpha():
            char_counts[each] = char_counts.get(each, 0) +1    
    return char_counts

def sort_on(dict):
    return dict["num"]

def dict_to_list(char_counts):
    return [{'char': char, 'num': count} for char, count in char_counts.items()]

def sort_char(char_counts_list):
    return sorted(char_counts_list, key=sort_on, reverse=True)