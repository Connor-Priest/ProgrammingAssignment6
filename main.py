# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pig_latin():
    sentence = input('Enter a Sentence: ')
    sentence = sentence.split()
    pig_sentence = []

    for word in sentence:
        if word[0] in ["a", "e", "i", "o", "u"]:
            pig_word = word+"yay"
            pig_sentence.append(pig_word)
        else:
            pig_word = word[1:] + word[0] + "ay"
            pig_sentence.append(pig_word)

    pig_sentence = " ".join(pig_sentence)
    print(pig_sentence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pig_latin()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
