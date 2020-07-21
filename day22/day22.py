"""Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a
list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should
return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either [
'bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']. """

from collections import defaultdict

def find_reconstructions(sentence: str, words: list):
    sentences = [sentence]
    results = [""]
    found = True
    final_results = []

    while found:
        found = False
        new_sentences = []
        new_results = []

        for word in words:
            for sentence_ in sentences:
                if sentence_.startswith(word):
                    found = True
                    new_sentences.append(sentence_[len(word):])
                    for result in results:
                        if result.replace(" ", "") + sentence_ == sentence:
                            if result.replace(" ", "") + word == sentence:
                                if len(result):
                                    final_results.append(result + " " + word)
                                else:
                                    final_results.append(word)
                            else:
                                if len(result):
                                    new_results.append(result + " " + word)
                                else:
                                    new_results.append(word)


        if found:
            sentences = new_sentences
            results = new_results
    return final_results

words = ['the', 'quick', 'brown', 'fox']
sentence = "thequickbrownfox"

print(find_reconstructions(sentence, words))

words_2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence_2 = "bedbathandbeyond"

print(find_reconstructions(sentence_2, words_2))
