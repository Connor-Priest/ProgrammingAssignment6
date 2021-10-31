# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys


def argumentReader():
    print("Number of Arguments: ", len(sys.argv))
    print("Argument List: ", str(sys.argv))


def HelloThere():
    f = open("HelloThere.txt", "a")
    f.write("Hello There")
    f.close()
    f = open("HelloThere.txt", "r")
    print(f.read())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    argumentReader()
    HelloThere()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
