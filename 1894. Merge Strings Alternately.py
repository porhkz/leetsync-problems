class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest = len(word2)
        tmp = []

        if len(word1) > len(word2):
            longest = len(word1)

        for itr in range(longest):
            if itr < len(word1):
                tmp.append(word1[itr])

            if itr < len(word2):
                tmp.append(word2[itr])

        return "".join(tmp)