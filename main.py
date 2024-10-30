
def main():
    with open("frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    wd_count = len(text.split())
    print(f"Word count: {wd_count} \n")

def char_count(text):
    char_frequencies = {}
    string = text.lower()
    
    for char in string:
        if char.isalpha():
            if char in char_frequencies:
                char_frequencies[char] += 1
            else:
                char_frequencies[char] = 1
        
    for char in char_frequencies:
        print(f"The letter '{char}' appears {char_frequencies[char]} times \n")

print("\n======= Starting analysis of 'frankenstein.txt' =======\n")

word_count(main())

char_count(main())

print("======= Analysis of 'frankenstein.txt' complete =======\n")