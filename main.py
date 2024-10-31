# Get the document for analysis
def main():
    with open("frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

# Word count of the document
def word_count(text):
    wd_count = len(text.split())
    print(f"{wd_count} words appear in the document\n")

# What to base the sort on
def sort_on(dict):
    return dict["count"]

# Count the alpha characters and provide their frequencies of appearance
def char_count(text):
    char_frequencies = {}
    string = text.lower()
    
    # Count character frequencies
    for char in string:
        if char.isalpha():
            if char in char_frequencies:
                char_frequencies[char] += 1
            else:
                char_frequencies[char] = 1

    # Put frequencies into a list of dictionaries
    char_list = []
    for char, freq in char_frequencies.items():
        char_list.append({"char":char, "count":freq})

    # Sort the list
    char_list.sort(reverse=True, key=sort_on)

    # (NEED TO UPDATE) Print frequency analysis to the console
    for char_dict in char_list:
        print(f"The letter '{char_dict['char']}' appears {char_dict['count']} times \n")





# Start program

print("\n======= Starting analysis of 'frankenstein.txt' =======\n")

word_count(main())

char_count(main())

print("======= Analysis of 'frankenstein.txt' complete =======\n")