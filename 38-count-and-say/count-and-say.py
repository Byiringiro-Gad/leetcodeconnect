class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        cnt = 1

        while cnt < n:
            cur = ""
            i = 0

            while i < len(curr):
                j = i
                while j < len(curr) and curr[j] == curr[i]:
                    j += 1
                
                cur += str(j - i) + curr[i]
                i = j

            curr = cur
            cnt += 1

        return curr
            
            
