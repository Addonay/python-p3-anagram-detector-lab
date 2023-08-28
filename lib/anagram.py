# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word)

        for candidate in word_list:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word and sorted(candidate_lower) == sorted_word:
                anagrams.append(candidate)

        return anagrams


listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result) 
