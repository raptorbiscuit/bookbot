
#!/usr/bin/python



def main():
    bookLocation = "./books/frankenstein.txt"
    print(f"--- Begin report of {bookLocation} ---")
    book = openBook(bookLocation)
    chars = countCharacters(book)
    charReport = printCharacterCount(chars)
    print(f"--- End report ---")

def openBook(bookPath):
    # open book and read
    with open(bookPath) as f:
        book = f.read().lower()

    # count number of words in the book
    bookLength = len(book.split())

    # print book length
    print(f'{bookLength} words found in the document\n')

    # return for us in countCharacters()
    return book

def countCharacters(book):
    charDict = {}

    # loop through every character and set value to charDict dictionary
    for chars in book:
        if chars in charDict:
            charDict[chars] += 1
        else:
            charDict[chars] = 1
    return charDict

def printCharacterCount(charCount):
    alphaList = []

    # filter out non-alpha characters
    for i in charCount:
        if i.isalpha():
            alphaList.append([i,charCount[i]])
            
    # sort and print results
    alphaList.sort()
    for each in alphaList:
        print(f"The {each[0]} character was found {each[1]} times")
    


if __name__ == '__main__':
    main()