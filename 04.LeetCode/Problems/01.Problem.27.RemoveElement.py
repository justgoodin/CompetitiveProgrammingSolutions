#Link to the question below
#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break