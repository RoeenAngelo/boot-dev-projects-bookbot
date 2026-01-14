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