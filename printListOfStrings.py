cities = ["austin", "dallas", "houston", "san antonio", "fort worth"]

def isListOfStrings(lst):
    if lst and isinstance(lst, list):
        return all(isinstance(elem, str) for elem in lst)
    else:
        return False

def printList(values):
    for value in values:
        print(value)

def properName(words):
    if isinstance(words, list) and isListOfStrings(words):
        printList([word.title() for word in words])
    else:
        print("The function properName() only accepts a list of strings as input.")

cities_capitalized = properName(cities)
