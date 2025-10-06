from typing import List
from collections import Counter

class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        # Count how many times each number appears using Counter
        # Counter(nums).items() returns pairs like (number, count)
        
        # max(..., key=lambda x: x[1]) finds the pair with the highest count
        # [0] gives the number (not the count), which is our majority element

        return max(Counter(nums).items(), key=lambda x: x[1])[0]