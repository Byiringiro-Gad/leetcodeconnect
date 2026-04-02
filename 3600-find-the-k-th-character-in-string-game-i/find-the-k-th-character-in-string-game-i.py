class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabets = {i:chr(i) for i in range(ord("a"), ord("z")+1)}
        def helper(word):
            if len(word) >= k:
                return word
            new = ""
            for c in word:
                new += alphabets[(ord(c)+1)% 97 + 97]
            return helper(word + new)
        word = helper("a")
        return word[k-1]
        