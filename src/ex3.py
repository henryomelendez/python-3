
def create_files(file_name):
    small_words = set()
    large_words = set()

    with open(f"../files/{file_name}", "r") as file:
        for line in file:
            for word in line.split():
                clean_word = word.strip('.,!?')

                if len(clean_word) < 3 :
                    small_words.add(clean_word)
                else:
                    large_words.add(clean_word)
    with open('small-words.txt', 'w') as  file:
        for word in sorted(small_words):
            file.write(word + '\n')
    with open('large-word.txt', 'w') as file:
        for word in sorted(large_words):
            file.write(word + '\n')
    return len( small_words | large_words)



def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")

ex3()