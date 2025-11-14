

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}

    for char in text:
        char = char.lower()

        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars
        
def prepare_dict_for_printing(dict_to_prepare):
    value_list = []
    
    def sort_on(items):
        return items["count"]

    for key in dict_to_prepare:
        value_list.append({ "char": key, "count": dict_to_prepare[key] })

    value_list.sort(reverse=True, key=sort_on)

    return value_list
        
def print_report(words_count, chars_dict):
    print("============ BOOKBOT ============ \n Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for i in range(len(chars_dict)):
        char = chars_dict[i]["char"]
        if char.isalpha():
            char_count = chars_dict[i]["count"]
            print(f"{char}: {char_count}")
    print("============= END ===============")
