import sys

def get_num_words(text):
    words = text.split()
    return len(words)

# convert text into a list.
# loop through the list and count letter
# make sure to include spaces and symbols
# all letters should be lowercase
#return a dictionary with letter as key and count as value

def get_num_letters(text):
    text = text.lower()
    letter_counts = {}
    text_list = list(text)

    for char in text_list:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list