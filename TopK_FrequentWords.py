from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        answer = Counter(words)
        hashT = defaultdict(list)
        for value, key in answer.items():
            hashT[key].append(value)
            hashT[key].sort()
        output = []
        for key in sorted(hashT.keys(),reverse=True):
            output += hashT[key]
        
        return output[:k]
