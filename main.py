with open("books/frankenstein.txt") as f:
    file = f.read()
    lowerfile =  file.lower()
    words = file.split()
    length = len(words)
    characters = {}
    for character in file:
        lower = character.lower()
        if lower.isalpha():  # Check if the character is alphabetic
            if lower in characters:
                characters[lower] += 1
            else:
                characters[lower] = 1
    print(file)

    print("Document is " + str(length) + " words long.")
    
    # Convert dictionary to list of tuples and sort by frequency
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    
    # Print the sorted characters with the desired message
    for char, count in sorted_characters:
        print(f"The character '{char}' was found {count} times.")

