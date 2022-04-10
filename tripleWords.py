"""Given an sentence string such as "Dooddley pupp carol yummyyy" what is the number of 
words that contain a triple i.e at least 3 instances of a letter.
"""
def tripleWords(sentence: str) -> int:
    words = sentence.split()
    print(words)
    count = 0
    for word in words:
        for letters in word.lower():
            if word.lower().count(letters) >= 3:
                count += 1
                break
    return count

tripleWords("Dooddley pupp carol yummyyy")