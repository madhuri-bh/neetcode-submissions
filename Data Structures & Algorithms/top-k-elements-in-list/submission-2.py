class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        
        for n in nums:
            frequencyMap[n] = 1 + frequencyMap.get(n, 0)
        sortedFreqMap = sorted(frequencyMap.items(), key= lambda num: num[1], reverse = True)
        return [num for num, frequency in sortedFreqMap[:k]]
            
        
