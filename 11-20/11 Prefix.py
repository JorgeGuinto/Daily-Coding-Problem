"Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix."
"For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]."
"Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."

def listWithPrefix (x, prefix):
    i = 0
    y = x.copy()
    while i < len(y):
        if (y[i].find(prefix) != 0):
            y.remove(y[i])
        else:
            i = i + 1
    return y


x = ["dog", "deer", "deal"]
print(listWithPrefix(x, "de"))
print(x)
