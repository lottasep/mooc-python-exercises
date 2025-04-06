story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")

    if word != "end" and word != previous_word:
        story += word + " "
        previous_word = word
    else:
        break

print(story.strip()) # strip ottaa välilyönnin lopusta pois