def count_words(file_contents):
    x = file_contents.split()
    return len(x)

dict_of_chars = {}
list_of_alpha = {}

def count_chars(file_contents):
    x = file_contents.lower()
    for char in x:
        
        if char not in dict_of_chars:
            dict_of_chars[char] = 1

        else:
            dict_of_chars[char] += 1

    return dict_of_chars

def only_alpha_dict(dict_of_chars):
    only_alpha = {}
    for key, value in dict_of_chars.items():
       if key.isalpha():
           only_alpha[key] = value
       else:
           pass

    return only_alpha

def sort_on(dict):
    return dict["num"]

def sorted_list(dict_of_chars):
    list_of_alpha = []
    for key, value in dict_of_chars.items():
        dict_of_alpha = {"char": key, "num": value}
        list_of_alpha.append(dict_of_alpha)
    list_of_alpha.sort(reverse=True, key = sort_on)
    return list_of_alpha


    



