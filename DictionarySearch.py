# Nkafu's Search Dictionary

# This function is responsible for separating
# the words from the definitions in the given
# line from the dictionary
def split(line):
    w = line.split("  ", 1)
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(w) != 1:
        for i in nums:
            if i in w[0]:
                w[0] = w[0].replace(i, '')
    w[0] = w[0].lower()
    return w


def main():
    file = open("smallDict.txt", "r")
    myDict = dict()

    for line in file:
        word = split(line)
        if word is not None and len(word) != 1:
            if word[0] in myDict:
                myDict[word[0]] = myDict[word[0]] + '\n' + word[0] + '  ' + word[1]
            else:
                myDict[word[0]] = word[1]

    fword = ""
    while fword != '%':
        fword = input("Enter a word you wish to find (Enter % to quit): ")
        if fword.lower() in myDict:
            print(fword, myDict[fword.lower()])
        else:
            print("Sorry not found!")


main()
