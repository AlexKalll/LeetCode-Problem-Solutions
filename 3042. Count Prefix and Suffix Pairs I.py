# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

def isPrefixAndSuffix(str1: str, str2: str) -> bool:
    return str2.startswith(str1) and str2.endswith(str1)
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
                    
        return count