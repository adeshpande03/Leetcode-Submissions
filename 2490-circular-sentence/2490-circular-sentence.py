class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        sentence = [sentence[-1]] + sentence
        trueCond = [sentence[i][-1] == sentence[i + 1][0] for i in range(len(sentence) - 1)]
        return all(trueCond)