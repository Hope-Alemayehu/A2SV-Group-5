class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word1 = s1.split()
        word2 = s2.split()

        all_words = word1 + word2

        word_count = Counter(all_words)
        return [word for word in word_count if word_count[word] == 1]