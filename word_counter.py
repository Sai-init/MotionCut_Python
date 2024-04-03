def word_count(sentence):
    words = sentence.split()
    return len(words)
def enter():
    sentence = input("Please enter a sentence or paragraph: ")
    if not sentence.strip():
        print("Error: Empty input! Please enter some input.")
    else:
        count = word_count(sentence)
        print(f"Word count : {count}")
enter()
