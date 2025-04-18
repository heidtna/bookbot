def get_num_words(string):
    word_list = string.split()
    return len(word_list)

def get_character_instances(string):
    letter_dict = {}
    string = string.lower()

    for ch in string:
        if ch in letter_dict:
            letter_dict[ch] += 1
        else:
            letter_dict[ch] = 1
    
    return letter_dict

def print_full_report(path_to_book, word_count, dict):  
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path_to_book}...")

    print("---------- Word Count ---------")
    print(f"Found {word_count} total words")
    
    print("------- Character Count -------")

    # print count of each LETTER in descending order (exclude special characters)
    for item in sort_by_count(dict):
        print(f"{item["letter"]}: {item["count"]}")

    print("============= END =============")    

def sort_by_count(dict):
    letter_list = []
    for key in dict:
        if key.isalpha():
            letter_list.append({"letter": key, "count": dict[key]})
    
    letter_list.sort(reverse= True, key=sort_on)
    return letter_list

def sort_on(dict):
    return dict["count"]