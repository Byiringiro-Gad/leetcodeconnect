class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1:
            return [i for i in range(10)]
        
        curr = [i for i in range(1, 10)]
        
        for _ in range(n - 1):
            next_level = []
            
            for num in curr:
                last_digit = num % 10
                
                next_digits = set()
                next_digits.add(last_digit + k)
                next_digits.add(last_digit - k)
                
                for next_digit in next_digits:
                    if 0 <= next_digit <= 9:
                        next_level.append(num * 10 + next_digit)
            
            curr = next_level
        
        return curr