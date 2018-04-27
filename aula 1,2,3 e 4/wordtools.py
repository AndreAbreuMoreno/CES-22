def cleanword(a):
    word = ""
    punctaction = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    for letter in a:
        if letter == "-":
            word += " "
        elif letter not in punctaction:
            word += letter
    return word

def has_dashdash(w):
    bool = 0
    for letter in w:
        if letter == "-":
            bool += 1
        else:
            bool = 0
        if bool == 2:
            return 1
    return 0

def extract_words(w):
    w = cleanword(w)
    words = w.lower()
    return words.split()

def wordcount(p,q):
    count = 0
    for word in q:
        if p == word:
            count += 1
    return count

def wordset(w):
    list = []
    i = 0
    for word in w:
        if word not in list:
            list.append(word)
            i += 1
    list.sort()
    return list

def longestword(w):
    count = 0
    for word in w:
        sz = len(word)
        if sz>count:
            count = sz
    return count

def test(a,b):
    if a == b:
        print("true")
    else:
        print("falso")

