"This problem was asked by Microsoft."
"Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null."
"For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string \"thequickbrownfox\", you should return ['the', 'quick', 'brown', 'fox']."
"Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string \"bedbathandbeyond\", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']."

def getSentenceList(words, sentence):
    n = []
    result = []

    for word in words:
        if len(word) not in n:
            n.append(len(word))
    i = 0
    while i < len(sentence):
        founded = False
        for j in n:
            if sentence[i:i+j] in words:
                result.append(sentence[i:i+j])
                i += j
                founded = True
                break
        if not founded:
            return None
    return result


words = ["quick", "brown", "the", "fox", "theq"]
sentence = "thequickbrownfox"

words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence2 = "bedbathandbeyond"

print(getSentenceList(words, sentence))
print(getSentenceList(words2, sentence2))