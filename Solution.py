from typing import List

class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize candidate and its count
        candidate: int = 0
        count: int = 0

        # Traverse through all elements in the array
        for currentElement in nums:
            # If count drops to zero, pick a new candidate
            # Like, "Alright, you look promising, I'll give you a chance!" 🤝
            if count == 0: candidate = currentElement
                
            # If current element is same as candidate, increase count
            # Otherwise, decrease count
            count += 1 if candidate == currentElement else -1
            # It's like voting: candidate gains votes if same, loses votes if different 🗳️

        # After one full pass, candidate is guaranteed to be majority element
        return candidate