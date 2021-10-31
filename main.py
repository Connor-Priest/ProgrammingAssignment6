# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def input1():
    sentence = input("Enter a sentence: ")
    for words in sentence.split():
        print(words)


def input2():
    sentence = input("Enter a sentence: ")
    words = sentence.replace(" ", "\n")
    print(words)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input1()
    input2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
