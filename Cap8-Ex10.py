def reverse(w):
    sz = len(w)
    i = 0
    rev = ""
    while i < sz:
        rev += w[sz - 1 - i]
        i += 1
    return rev

def is_palindrome(w):
    rev = reverse(w)
    if w == rev:
        print("is_palindrome({})".format(w))
    else:
        print("not is_palindrome({})".format(w))

def teste(w):
    is_palindrome(w)

teste("abba")
teste("abab")
teste("tenet")
teste("banana")
teste("straw warts")
teste("a")
teste(" ")


