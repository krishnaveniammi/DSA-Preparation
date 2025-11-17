class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        res =[]
        words = (s1 + " " + s2).split()
        for word in words:
            if words.count(word) == 1 :
                res.append(word)
        return res